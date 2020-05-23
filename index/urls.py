from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room>/', views.room, name='room'),
    path('about', views.about, name="about"),
    path('signup', views.signup, name="signup"),
    path('painting/<str:painting_name>/', views.painting, name='painting'),
    path('unnamed', views.unnamed, name='unnamed'),
    path('view_painting', views.view_painting, name='view_painting'),
    path('painting_guess', views.painting_guess, name='painting_guess'),
    path('reset', views.reset, name='reset'),
    path('detect_browser/', views.detect_browser, name='detect_browser'),
    path('adventure/', views.adventure, name='adventure'),
]
