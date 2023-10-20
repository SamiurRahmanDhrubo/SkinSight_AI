from django.db import models
from django.contrib.auth.models import User






class PaymentRequest(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    payment_status = models.BooleanField(default=False)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    payment_status = models.BooleanField(default=False)
    value = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    result_history = models.ManyToManyField('ResultHistory', related_name='user_profiles', blank=True)

    def __str__(self):
        return self.user.username


class ResultHistory(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='result_history_images/')
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')






