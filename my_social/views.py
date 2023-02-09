from django.shortcuts import render
from .models import User, Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'my_social/post_list.html', {'posts': posts})

