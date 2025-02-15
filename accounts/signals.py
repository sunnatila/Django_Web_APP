from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            email=instance.email
        )
    else:
        profile = get_object_or_404(Profile, user=instance)
        profile.email = instance.email
        profile.save()


@receiver(post_save, sender=Profile)
def update_user_profile(sender, instance, created, **kwargs):
    profile = instance
    if not created:
        user = get_object_or_404(CustomUser, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()
