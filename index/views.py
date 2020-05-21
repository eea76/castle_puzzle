from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import json

from .models import *


def ground_floor(request):
    obj = {}
    return render(request, 'index.html', obj)

@login_required
def balcony_front(request):
    obj = {}
    return render(request, 'balcony_front.html', obj)

@login_required
def balcony_overhead(request):
    obj = {}
    return render(request, 'balcony_overhead.html', obj)

@login_required
def painting(request, id):
    painting = Painting.objects.get(id=id)
    obj = {
        'painting': painting
    }

    return render(request, 'painting.html', obj)

@login_required
def unnamed(request):
    viewed_paintings = UserPainting.objects.filter(user=request.user)
    viewed_paintings_count = len(viewed_paintings)
    correct_name = 'vividarium intervigilium viator'
    english = 'In the Garden Sleeps a Messenger'
    latin = 'Vividarium et Intervigilium et Viator'

    obj = {
        'viewed_paintings': viewed_paintings,
        'correct_name': correct_name,
        'english': english,
        'latin': latin,
        'viewed_paintings_count': viewed_paintings_count,
    }

    return render(request, 'unnamed.html', obj)


#######

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    obj = {
        'form' : form,
    }

    return render(request, 'registration/signup.html', obj)


@csrf_exempt
def view_painting(request):

    try:
        data = json.loads(request.body)
        painting_id = data['paintingId']


        if painting_id != 'unnamed':
            painting = Painting.objects.get(id=painting_id)
            user_painting = UserPainting.objects.get_or_create(
                user=request.user,
                painting=painting,
                viewed=True)

            user_painting.save()
        else:
            print('fuck')

    except Exception as e:
        print('-------')
        print("unable to do this for the following reason:")
        print(e)
        print('-------')

    return HttpResponse("Success")


@csrf_exempt
def painting_guess(request):
    try:
        data = json.loads(request.body)
        guess = data['guess']

        correct_name = 'vividarium intervigilium viator'
        guess = guess.strip().lower()

        new_guess = Attempt()
        new_guess.user = request.user
        new_guess.guess = guess

        new_guess.save()

        if guess == correct_name:
            answer = {
                'correct': True,
                'correct_name': 'vividarium intervigilium viator',
                'english': 'In the Garden Sleeps a Messenger',
                'latin': 'Vividarium et Intervigilium et Viator',
                'image': "https://ultimeciacastle.s3-us-west-2.amazonaws.com/screens/unnamed.jpg",
            }

            return HttpResponse(json.dumps(answer))
        else:
            answer = {
                'correct': False
            }
            return HttpResponse(json.dumps(answer))

    except Exception as e:
        print('-------')
        print("unable to do this for the following reason:")
        print(e)
        print('-------')


def reset(request):
    viewed_paintings = UserPainting.objects.filter(user=request.user)
    for view_painting in viewed_paintings:
        view_painting.delete()

    return redirect('/unnamed')
