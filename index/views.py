from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):

    obj = {}

    return render(request, 'index.html', obj)
