from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Rapper

from django.core.mail import send_mail
from django.conf import settings