from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    # path('accounts/login/', views.userlogin, name='userlogin'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/<int:user_id>/edit/',views.profile_edit, name='edit'),
    path('accounts/profile/<int:blog_id>/', views.blog, name='blog'),
]