from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import Http404
from django.db.models import Count 
from django.core.mail import send_mail
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag


def post_list(request: str, tag_slug: str = None) -> tuple:
    post_list = Post.published.all()
    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
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
                    {'posts': posts,
                    'tag': tag,})


def post_detail(request: str, year: int, month: int, day: int, post: str) -> tuple:
    
    post = get_object_or_404(Post, 
                                status = Post.Status.PUBLISHED,
                                slug=post, 
                                publish__year=year, 
                                publish__month=month, 
                                publish__day=day)
    # full list comment to post 
    comments = post.comments.filter(active=True)
    # form for comments
    form = CommentForm()

    # tegs
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]


    return render(request, 
                    'blog/post/detail.html', 
                    {'post': post,
                    'comments': comments, 
                    'form': form,
                    'similar_posts': similar_posts,})


def post_share(request: str, post_id: int):
    """Shareing posts for email."""

    # post from id 
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    # mail flag
    sent = False
    # testing methods in form
    if request.method == 'POST':
        # form send 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # validation success
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f'{cd["name"]} recommends you read f{post.title}'
            message = f'Read {post.title} at {post_url}\n\n {cd["name"]} comments -> {cd["comments"]}'
            send_mail(subject, message, 'testuser@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post, 
        'form': form,
        'sent': sent,
    })

# comments 
@require_POST
def post_comment(request: str, post_id: int):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # sent 
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # create Comment will not save in db 
        comment = form.save(commit=False)
        # post to comment
        comment.post = post
        # save
        comment.save()
    return render(request, 'blog/post/comment.html', 
                        {'post': post, 'form': form, 'comment': comment,})