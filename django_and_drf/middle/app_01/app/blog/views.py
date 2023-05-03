from django.shortcuts import render
from django.http import Http404
from .models import Post

def post_list(request: str) -> tuple:
    posts = Post.published.all()
    return render(request, 
                    'blog/post/list.html',
                    {'posts': posts,})


def post_detail(request: str, id: int) -> tuple:
    
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post Found in blog')

    return render(request, 
                    'blog/post/detail.html', 
                    {'post': post,})
                    
