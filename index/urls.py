from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('', views.ground_floor, name='ground_floor'),
    path('balcony_front', views.balcony_front, name='balcony_front'),
    path('balcony_overhead', views.balcony_overhead, name='balcony_overhead'),
    path('painting/<int:id>/', views.painting, name='painting'),
    path('unnamed', views.unnamed, name='unnamed'),
    path('view_painting', views.view_painting, name='view_painting'),
    path('painting_guess', views.painting_guess, name='painting_guess'),
]
