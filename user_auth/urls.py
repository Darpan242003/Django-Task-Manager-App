from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.user_logout, name='logout'),
    path('update', views.update_profile, name='update'),
    path('password', views.change_pass, name='password'),
]
