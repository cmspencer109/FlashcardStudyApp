from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#   if created:
#     Student.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#   instance.student.save()



