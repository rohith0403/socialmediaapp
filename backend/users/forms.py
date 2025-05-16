from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """This class adds email to the User register form"""

    email = forms.EmailField()

    class Meta:
        """
        This class gives us a nested namespace
        for our configurations and keeps the configurations
        in one place.
        """

        model = User
        fields = ["username", "email", "password1", "password2"]
