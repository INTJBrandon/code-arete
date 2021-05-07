from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/newer', views.newer, name='blog-newer'),
    path('posts/older', views.older, name='blog-older'),
    path('posts/<int:id>', views.post_detail, name='blog-detail'),
    

]