from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PostListView(ListView):
    """Alter views list of posts."""

    queryset = Post.published.all()
    content_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


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

