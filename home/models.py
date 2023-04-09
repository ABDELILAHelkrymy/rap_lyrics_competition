from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.db.models.signals import post_save

class Rapper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rapper')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    awards = models.TextField(max_length=500, blank=True)
    trophies = models.TextField(max_length=500, blank=True)
    links = models.TextField(max_length=500, blank=True)
    recommendations = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(
        blank=True, null=True, 
        upload_to = 'profiles/',
        default ='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.user.username

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Song(models.Model):
    rapper = models.ForeignKey(Rapper, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)

    def __str__(self):
        return self.title
    

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):

    if created:
        user = instance
        rapper = Rapper.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            first_name = user.first_name,
        )

post_save.connect(createProfile, sender=User)