from django.contrib import admin
from .models import Rapper, Song, Recommandations

admin.site.register(Rapper)
admin.site.register(Song)
admin.site.register(Recommandations)
