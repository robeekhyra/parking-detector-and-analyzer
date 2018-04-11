from datetime import datetime
from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Parking

status = ''
counter = 0
statuses = []

# Create your views here.
def index(request):
    return render(request, 'index.html')

def increment(request):
    global status
    status = [int(stat) for stat in list(status)]
    sensorHandler()

    try:
        suggestion = status.index(0) + 1
    except ValueError:
        suggestion = 'None'

    context = {
        'status': status,
        'available': len(status)-sum(status),
        'suggestion': suggestion
               }
    return JsonResponse(context)


def sensorHandler():
    handle(counter, status, statuses)


def handle(counter, status, statuses):
    if counter == 0:
        statuses = [[] for i in range(len(status))]
    elif counter != 10:
        for i in range(len(status)):
            statuses[i].append(status[i])
    elif counter == 10:
        for i in range(len(status)):
            if len(set(statuses[i])) == 1:
                slot = i + 1
                parking = Parking.objects.filter(slotID=slot).order_by('-id').first()

                if parking.exists():
                    pass
                elif parking.timeOut is None:
                    pass
                else:
                    parking = Parking(slotID=slot, timeIn=datetime.now())
                    parking.save()

    counter += 1