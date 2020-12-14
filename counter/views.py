from django.shortcuts import render
from django.http import JsonResponse
from .models import Visits
from datetime import date, datetime, time, timedelta, timezone
import pytz


# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_daydata(request):
    timebox = float(request.GET["time"])

    date_from = datetime.now() - timedelta(hours=timebox)
    last_24 = Visits.objects.all()
    tz = pytz.timezone("Europe/Zurich")
    daydata = []
    for dta in last_24:
        if dta.added > tz.localize(date_from):
            daydata.append(dta.current_loggedin)

    open = False
    if date.today().weekday() == 0:
        open = time(13, 00) <= datetime.now().time() <= time(19, 00)
    if 0 < date.today().weekday() < 6:
        open = time(9, 00) <= datetime.now().time() <= time(19, 00)
    last_insert = Visits.objects.latest('added')

    data = {
        'daydata': daydata,
        'open': open,
        'free': last_insert.current_free,
        'visitors': last_insert.current_loggedin,
        'trend': calc_trend()
    }

    return JsonResponse(data)


def calc_trend():
    last_visits = Visits.objects.all().order_by('-added')[:11]

    last = last_visits[0].current_loggedin

    middle = 0

    for p in last_visits[1:]:
        middle = middle + int(p.current_loggedin)

    middle = middle / 10
    last = float(last)
    trend = ""

    if last < middle:
        trend = "down"
    elif last == middle:
        trend = "stable"
    elif last > middle:
        trend = "up"

    return trend


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time
