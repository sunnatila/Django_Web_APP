from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Foydalanuvchi yaratilganda Profile yaratish
    else:
        # Agar foydalanuvchi mavjud bo'lsa va Profile yo'q bo'lsa, uni yaratish
        instance.profile, created = Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()  # Foydalanuvchi saqlanganda Profile ham saqlansin

