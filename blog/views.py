from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.published.all()

    return render(request, 'list.html', {'posts' : posts})

# def post_detail(request, id):
def post_detail(request, year, month, day, post):
    # post = Post.published.get(id=id)
    post = Post.published.get(slug=post,publish__year=year,publish__month=month,publish__day=day)

    return render(request, 'detail.html', {'post' : post})
    
