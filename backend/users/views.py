# Django provides base templates for user registration forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        # If the request method is post request, instantiates with post data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the registered user in DB
            form.save()
            # To get username
            # username = form.cleaned_data.get("username")
            # Flashed message. Sent to the template. Happens only once (the first time)
            messages.success(request, "Your account has been created! Please login.")
            # Return a redirect to the blog-home after account creation
            return redirect("")

    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """View for the user profile page."""
    return render(request, "users/profile.html")
