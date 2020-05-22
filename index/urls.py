from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('', views.ground_floor, name='ground_floor'),
    path('signup', views.signup, name="signup"),
    path('balcony_front', views.balcony_front, name='balcony_front'),
    path('balcony_overhead', views.balcony_overhead, name='balcony_overhead'),
    path('painting/<str:painting_name>/', views.painting, name='painting'),
    path('unnamed', views.unnamed, name='unnamed'),
    path('view_painting', views.view_painting, name='view_painting'),
    path('painting_guess', views.painting_guess, name='painting_guess'),
    path('reset', views.reset, name='reset'),
]
