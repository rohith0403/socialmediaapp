from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "author": "Corey MS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Aug 27 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "Aug 28 2018",
    },
]


# Create your views here.
def home(request):
    """Home response"""
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    """About response"""
    return render(request, "blog/about.html", {"title": "About"})
