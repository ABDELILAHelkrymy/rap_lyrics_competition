from django.urls import path

from . import views

urlpatterns = [
    path('', views.competitions, name='competitions'),
    path('create-competition/', views.createCompetition, name='create-competition'),
    path('update-competition/<str:pk>/', views.updateCompetition, name='update-competition'),
    path('delete-competition/<str:pk>/', views.deleteCompetition, name='delete-competition'),
]
