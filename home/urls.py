from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rapper-register/', views.register, name='rapper-register'),
    path('rapper-profile/', views.rapperProfile, name='rapper-profile'),
    path('rapper-profile-view/<str:pk>/', views.getRapper, name='rapper-profile-view'),
    path('rapper-songs/', views.rapperSongs, name='rapper-songs'),
    path('rapper-song/<str:song_id>/', views.rapperSong, name='rapper-song'),
    path('edit-song/<str:song_id>/', views.rapperSongEdit, name='edit_song'),
    path('delete-song/<str:song_id>/', views.rapperSongDelete,name='delete_song'),
    path('rappers-profile/', views.rappersProfileList, name='rappers-profile'),
    path('rapper-login/', views.CustomLoginView.as_view(), name='rapper_login'),
    path('rapper-logout/', views.user_logout_view_custom, name="logout_custom")
]
