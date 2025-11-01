from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null = True, blank = True)
    profile_pic= models.ImageField(upload_to = "media/", null = True, blank = True)
    Designation = models.CharField(null = True, blank = True,  default="Student")

    def __str__(self):
        return self.user.username
