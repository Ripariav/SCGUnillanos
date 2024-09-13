from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.homeview, name='home'),
    path('contract/', views.contractview, name='contract'),
    path('profile/', views.profileview, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('superuser/', views.create_superuser, name='create_superuser'),
]