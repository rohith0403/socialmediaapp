# from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


# Create your views here.
def home(request):
    """Home response"""
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    """About response"""
    return render(request, "blog/about.html", {"title": "About"})
