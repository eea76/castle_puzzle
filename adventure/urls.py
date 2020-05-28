from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('door/<int:chamber_id>', views.chamber, name="chamber"),
]
