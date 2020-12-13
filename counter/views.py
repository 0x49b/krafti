from django.shortcuts import render
from django.http import JsonResponse
from .models import Visits
from datetime import date, datetime, time, timedelta
import pytz
import json


# Create your views here.
def index(request):
    open = False
    if date.today().weekday() == 0:
        open = is_time_between(time(13, 30), time(19, 00))
    if 0 < date.today().weekday() < 6:
        open = is_time_between(time(9, 00), time(19, 00))

    last_insert = Visits.objects.latest('added')
    context = {
        'free': last_insert.current_free,
        'open': open
    }
    return render(request, 'index.html', context)


def get_daydata(request):
    date_from = datetime.now() - timedelta(days=1)
    last_24 = Visits.objects.all()
    tz = pytz.timezone("Europe/Zurich")
    daydata = []
    for dta in last_24:
        if dta.added > tz.localize(date_from):
            daydata.append(dta.current_loggedin)

    data = {
        'daydata': daydata
    }

    return JsonResponse(data)


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time
