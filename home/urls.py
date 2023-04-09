from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rapper-register/', views.register, name='rapper-register'),
    path('rapper-profile/', views.rapperProfile, name='rapper-profile'),
    path('rapper-songs/', views.rapperSongs, name='rapper-songs'),
    path('rapper-song/<str:song_id>/', views.rapperSong, name='rapper-song'),
    path('edit-song/<str:song_id>/', views.rapperSongEdit, name='edit_song'),
    path('delete-song/<str:song_id>/', views.rapperSongDelete,name='delete_song'),
]
