from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.order_by("-created_date")
    context  =  {'posts':posts}
    return render(request, 'blog/post_list.html', context)

