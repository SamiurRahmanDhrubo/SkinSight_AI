from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    # Add other fields as needed

    def __str__(self):
        return self.user.username


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
