from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('posts/', views.group_posts),
    path('group/<slug:slug>/', views.group_posts)
] 
