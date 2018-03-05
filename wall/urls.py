from django.urls import path

from . import views

app_name = 'wall'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.new_post, name='new_post'),
    path('posted/', views.posted, name='posted'),
]