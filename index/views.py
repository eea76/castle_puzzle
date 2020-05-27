import json
from datetime import datetime
from pytz import timezone

import sendgrid
from decouple import config
from sendgrid.helpers.mail import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone as django_timezone

from .models import *


def index(request):
    if request.user.is_authenticated:
        return redirect('/room/groundfloor')
    else:
        return render(request, 'index.html')


@login_required
def room(request, room):
    room = Room.objects.get(room=room)
    paintings = PaintingPerRoom.objects.filter(room=room)
    links = Link.objects.filter(room=room)

    obj = {
        'room': room,
        'paintings': paintings,
        'links': links,
    }

    return render(request, 'room.html', obj)


def about(request):
    return render(request, 'about.html')


def adventure(request):
    return render(request, 'adventure.html')


@login_required
def painting(request, painting_name):

    if painting_name != 'unnamed':
        painting = Painting.objects.get(name=painting_name)
        obj = {
            'painting': painting
        }

        return render(request, 'painting.html', obj)

    else:
        viewed_paintings = UserPainting.objects.filter(user=request.user)
        viewed_paintings_count = len(viewed_paintings)

        obj = {
            'viewed_paintings': viewed_paintings,
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

            admin_name = config('admin')
            admin = User.objects.get(username=admin_name)
            admin_email = config('admin_email')
            username = str(user.username)
            send_email(admin.email, 'New user on castle escape room!!', f'{username} registered', admin_email)
            return redirect('/')
    else:
        form = UserCreationForm()

    obj = {
        'form' : form,
    }

    return render(request, 'registration/signup.html', obj)


# sendgrid
def send_email(email, subject, message, from_email):
    apikey = config('SENDGRID_API_KEY')
    sg = sendgrid.SendGridAPIClient(apikey=apikey)
    from_email = Email(from_email)
    to_email = Email(email)
    content = Content("text/html", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


@csrf_exempt
def view_painting(request):
    try:
        data = json.loads(request.body)
        painting_name = data['paintingName']

        if painting_name != 'unnamed':
            painting = Painting.objects.get(name=painting_name)
            user_painting = UserPainting.objects.get_or_create(
                user=request.user,
                painting=painting,
                viewed=True)

            user_painting[0].save()
        else:
            redirect('/unnamed')

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

        timestamps = data['timestamps']
        guess = data['guess']

        painting_titles = [
            'VENUS',
            'XERAMPELINAE',
            'VIVIDARIUM',
            'IGNUS',
            'INANDANTIA',
            'IUDICIUM',
            'INTERVIGILIUM',
            'XIPHIAS',
            'VIGIL',
            'VIATOR',
            'INAUDAX',
            'XYSTUS'
        ]

        tried_to_hack = False

        split_guess = guess.strip().split(' ')
        for legit_title in split_guess:
            if legit_title in painting_titles:
                continue
            else:
                tried_to_hack = True


        correct_name = 'vividarium intervigilium viator'
        guess = guess.strip().lower()

        new_guess = Attempt()
        new_guess.user = request.user
        new_guess.guess = guess

        first_title = guess.split(' ')[0]
        first_title_timestamp = timestamps[0]
        second_title = guess.split(' ')[1]
        second_title_timestamp = timestamps[1]
        third_title = guess.split(' ')[2]
        third_title_timestamp = timestamps[2]

        new_guess.first_title = first_title
        new_guess.first_title_timestamp = first_title_timestamp
        new_guess.second_title = second_title
        new_guess.second_title_timestamp = second_title_timestamp
        new_guess.third_title = third_title
        new_guess.third_title_timestamp = third_title_timestamp

        new_guess.save()

        if guess == correct_name:
            answer = {
                'correct': True,
                'correct_name': 'vividarium intervigilium viator',
                'english': 'In the Garden Sleeps a Messenger',
                'latin': 'Vividarium et Intervigilium et Viator',
                'image': "https://ultimeciacastle.s3-us-west-2.amazonaws.com/screens/unnamed.jpg",
                'attempts_count': Attempt.objects.filter(user=request.user).count()
            }

            return HttpResponse(json.dumps(answer))

        elif tried_to_hack:
            answer = {
                'correct': False,
                'tried_to_hack': '!!! WTF !!! trying to hack the source code will not help you.'
            }

            return HttpResponse(json.dumps(answer))

        else:
            answer = {
                'correct': False,
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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def detect_browser(request):
    try:
        data = json.loads(request.body)
        browser = data['browser']
        operating_system = data['os']

        b = Browser.objects.get_or_create(name = browser)
        o = OperatingSystem.objects.get_or_create(name = operating_system)

        p = PageLoad()
        p.page = data['url']
        p.browser = b[0]
        p.operating_system = o[0]
        p.ip_address = get_client_ip(request)
        p.time_stamp = django_timezone.now()

        if request.user.is_authenticated:
            p.user = request.user

            if request.user.username != 'elon':
                p.save()


    except Exception as e:
        print("unable to detect browser")
        print(e)


    return HttpResponse("Success")
