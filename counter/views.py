import logging
from datetime import date, datetime, time, timedelta

import pytz
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from routes.models import Route
from .models import Visits, ModalInfo
from rest_framework import viewsets
from .serializers import VisitSerializer


logger = logging.getLogger(__name__)


class LastCounterViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to receive the last 11 visit number
    """
    queryset = Visits.objects.all().order_by('-added')[:11]
    serializer_class = VisitSerializer
    http_method_names = ['get']


def index(request):
    rts = Route.objects.filter(archived=False).order_by('category')
    info = ModalInfo.objects.filter(type="modal-html")

    cweek = datetime.today().isocalendar()[1]
    thisweekroutes = []
    lastweekroutes = []

    for rt in rts:
        if rt.date.isocalendar()[1] == cweek:
            thisweekroutes.append(rt)
        if rt.date.isocalendar()[1] == cweek - 1:
            lastweekroutes.append(rt)

    routes = [thisweekroutes, lastweekroutes]
    return render(request, 'index.html', {'routes': routes, 'modalinfo': info[0].info})


def get_daydata(request):
    timebox = float(request.GET["time"])
    date_from = datetime.now() - timedelta(hours=timebox)
    last_24 = Visits.objects.all().order_by('-added')[:int(timebox * 60)]
    tz = pytz.timezone("Europe/Zurich")
    daydata = []
    for dta in last_24:
        if dta.added > tz.localize(date_from):
            daydata.append(dta.current_loggedin)

    opening_times = {0: ("13:00", "22:00"), 1: ("09:00", "22:00"), 2: ("09:00", "22:00"), 3: ("09:00", "22:00"),
                     4: ("13:00", "22:00"), 5: ("09:00", "20:00"), 6: ("09:00", "20:00")}

    times = opening_times.get(date.today().weekday())

    start = times[0].split(":")
    end = times[1].split(":")
    open = time(int(start[0]), int(start[1])) <= datetime.now().time() <= time(int(end[0]), int(end[1]))
    last_insert = Visits.objects.latest('added')

    free = 0
    visitors = 0

    if not calc_perm_closed():
        free = last_insert.current_free
        visitors = last_insert.current_loggedin

    data = {
        'daydata': daydata,
        'open': open,
        'free': free,
        'visitors': visitors,
        'total': free + visitors,
        'trend': calc_trend(),
        'permanent_closed': calc_perm_closed(),
        'permanent_closed_date': get_perm_close_end_date()
    }

    return JsonResponse(data)


def get_perm_close_end_date():
    perm_closed = settings.PERMANENT_CLOSED.split(" ")
    return perm_closed[0]


def calc_perm_closed():
    perm_closed = datetime.strptime(settings.PERMANENT_CLOSED, '%d.%m.%Y %H:%M:%S')
    t_now = datetime.now() - perm_closed
    return not t_now > timedelta(0)


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
