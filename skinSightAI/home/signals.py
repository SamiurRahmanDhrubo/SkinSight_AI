# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PaymentRequest, UserProfile

@receiver(post_save, sender=PaymentRequest)
def update_user_profile(sender, instance, created, **kwargs):
    if created:  # Only perform this when a new PaymentRequest is created
        try:
            user_profile = UserProfile.objects.get(full_name=instance.full_name)
            user_profile.payment_status = instance.payment_status
            user_profile.save()
        except UserProfile.DoesNotExist:
            pass  # Handle the case where there is no matching UserProfile
