from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    # path('accounts/profile/blog/', views.blog, name='blog')
    path('accounts/profile/<int:blog_id>/', views.blog, name='blog')
]