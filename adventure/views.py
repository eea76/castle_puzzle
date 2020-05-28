from django.shortcuts import render, get_object_or_404, redirect

from .models import *


def index(request):
    doors = Door.objects.all()

    obj = {
        'doors': doors,
    }

    return render(request, 'doors.html', obj)



def chamber(request, chamber_id):
    chamber = Chamber.objects.get(id=chamber_id)
    options = Option.objects.filter(belonging_chamber=chamber_id)

    end = False
    if chamber.result:
        end = True

    obj = {
        'chamber': chamber,
        'options': options,
        'end': end,
    }

    if chamber.initial_chamber == False:
        previous_option = PreviousOption.objects.get(current_chamber=chamber)
        previous_chamber = previous_option.previous_chamber

        obj['previous_option'] = previous_option
        obj['previous_chamber'] = previous_chamber



    return render(request, 'chamber.html', obj)


def result(request, id):

    preceding_child = Child.objects.get(id=id)
    result = Result.objects.get(preceding_child=preceding_child)

    obj = {
        'result': result,
    }

    return render(request, 'result.html', obj)
