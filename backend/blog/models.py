# Import user
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# We are using Django's ORM to create a post class
class Post(models.Model):
    """Post class"""

    # for chars
    title = models.CharField(max_length=100)
    # For multi lin text
    content = models.TextField()
    # Not now() but now. We would like to send the fn not the value
    date_posted = models.DateTimeField(default=timezone.now)
    # Foreign Key - Delete posts on user deletion
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # This is to tell the program what to show when fetching
    # Post objects from DB
    def __str__(self) -> str:
        return self.title
