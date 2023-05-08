from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator

def post_list(request: str) -> tuple:
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

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

