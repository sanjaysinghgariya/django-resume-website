from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('languages/', views.languages, name='languages'),
    path('projects/', views.projects, name='Project')
]
