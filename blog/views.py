from django.shortcuts import render, get_object_or_404
from .models import import Post

def post_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})
