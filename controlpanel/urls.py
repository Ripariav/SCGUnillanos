from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeview, name='home'),
    path('profile/', views.profileview, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
