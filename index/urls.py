from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]
