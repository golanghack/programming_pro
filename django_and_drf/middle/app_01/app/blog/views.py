from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm


def post_list(request: str) -> tuple:
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 
                    'blog/post/list.html',
                    {'posts': posts,})


def post_detail(request: str, year: int, month: int, day: int, post: str) -> tuple:
    
    post = get_object_or_404(Post, 
                                status = Post.Status.PUBLISHED,
                                slug=post, 
                                publish__year=year, 
                                publish__month=month, 
                                publish__day=day)

    return render(request, 
                    'blog/post/detail.html', 
                    {'post': post,})


def post_share(request: str, post_id: int):
    """Shareing posts for email."""

    # post from id 
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    # testing methods in form
    if request.method == 'POST':
        # form send 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # validation success
            cd = form.cleaned_data
            # send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post, 
        'form': form,
    })

