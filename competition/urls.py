from django.urls import path

from . import views

urlpatterns = [
    path('', views.competitions, name='competitions'),
    path('create-competition/', views.createCompetition, name='create-competition'),
    path('update-competition/<str:pk>/', views.updateCompetition, name='update-competition'),
    path('delete-competition/<str:pk>/', views.deleteCompetition, name='delete-competition'),
    path('competition/<str:pk>/', views.competition, name='competition'),
    path('join-competition/<str:pk>/', views.joinCompetition, name='join-competition'),
    path('leave-competition/<str:pk>/', views.leaveCompetition, name='leave-competition'),
]
