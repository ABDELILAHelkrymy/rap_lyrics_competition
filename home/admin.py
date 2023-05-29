from django.contrib import admin
from .models import Rapper, Song, Recommandations, Message

admin.site.register(Rapper)
admin.site.register(Song)
admin.site.register(Recommandations)
admin.site.register(Message)