from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import NewUser

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    user.is_logged_in = True
    user.save()

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    user.is_logged_in = False
    user.save()
