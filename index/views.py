from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *


def ground_floor(request):

    obj = {}

    return render(request, 'index.html', obj)


def balcony_front(request):

    obj = {}

    return render(request, 'balcony_front.html', obj)


def balcony_overhead(request):

    obj = {}

    return render(request, 'balcony_overhead.html', obj)

def painting(request, id):

    painting = Painting.objects.get(id=id)

    obj = {
        'painting': painting
    }

    return render(request, 'painting.html', obj)


def unnamed(request):
    viewed_paintings = Painting.objects.filter(viewed=True)
    correct_name = 'vividarium intervigilium viator'
    english = 'In the Garden Sleeps a Messenger'

    obj = {
        'viewed_paintings': viewed_paintings,
        'correct_name': correct_name,
        'english': english,
    }

    return render(request, 'unnamed.html', obj)

@csrf_exempt
def painting_guess(request):
    try:
        data = json.loads(request.body)
        guess = data['guess']

        correct_name = 'vividarium intervigilium viator'
        guess = guess.strip().lower()

        if guess == correct_name:
            return HttpResponse("correct")
        else:
            return HttpResponse("incorrect")

    except Exception as e:
        print('-------')
        print("unable to do this for the following reason:")
        print(e)
        print('-------')

