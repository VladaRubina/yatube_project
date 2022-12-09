from django.urls import path

from . import views


urlpatterns = [
    #Главная страница
    path('', views.index),
    #Посты по группам
    path('posts/', views.group_posts),
    #ждем переменную типа slug
    path('group/<slug:slug>/', views.group_posts)
] 
