from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.daftar_blog, name='blog'),
    path('', views.home, name='home'),
    path('author/', views.author, name='author'),
    path('mentee/', views.daftar_mentee, name='mentee'),
    path('mentor/', views.daftar_mentor, name='mentor'),
    path('mentee/input/', views.input_mentee, name='input_mentee'),
    path('mentor/input/', views.input_mentor, name='input_mentor'),
    path('blog/input/', views.input_blog, name='input_blog'),
]