from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action
import redis
from django.conf import settings

# Redis
r = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


@login_required()
def image_create(request):
    if request.method == "POST":
        # send
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # OK
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # current user for element
            new_image.user = request.user
            new_image.save()
            create_action(request.user, "added image", new_image)
            messages.success(request, "You successfully added image")
            # redirect for detail
            return redirect(new_image.get_absolute_url())
    else:
        # get method building form with data
        form = ImageCreateForm(data=request.GET)
    return render(
        request, "images/image/create.html", {"section": "images", "form": form}
    )


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # union views for images
    total_views = r.incr(f"image:{image.id}:views")
    # raiting
    r.zincrby("image_rank", 1, image.id)
    return render(
        request,
        "images/image/detail.html",
        {
            "section": "images",
            "image": image,
            "total_views": total_views,
        },
    )


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action")

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
                create_action(request.user, "likes", image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse(
                {
                    "status": "ok",
                }
            )
        except Image.DoesNotExist:
            pass
        return JsonResponse(
            {
                "status": "error",
            }
        )


@login_required
def image_list(request):
    """QUery set all images from db"""

    images = Image.objects.all()
    paginator = Paginator(images, 6)
    page = request.GET.get("page")
    images_only = request.GET.get("images_only")

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # AJAX and page out range return empty page
            return HttpResponse("")
        # page out range return last page
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(
            request,
            "images/image/list_images.html",
            {
                "section": "images",
                "images": images,
            },
        )
    return render(
        request,
        "images/image/list.html",
        {
            "section": "images",
            "images": images,
        },
    )


@login_required
def image_ranking(request):
    # get dict for raiting
    image_rank = r.zrange("image_rank", 0, 1, desc=True)[:10]
    image_rank_ids = [int(id) for id in image_rank]
    # get most view image
    most_viewed_images = list(Image.objects.filter(id__in=image_rank_ids))
    most_viewed_images.sort(key=lambda x: image_rank_ids.index(x.id))
    return render(
        request,
        "images/image/rank.html",
        {
            "section": "images",
            "most_viewed_images": most_viewed_images,
        },
    )
