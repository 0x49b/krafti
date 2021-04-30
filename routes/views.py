from django.shortcuts import render
from .models import Route
from datetime import datetime


def testRouteList(request):
    rts = Route.objects.all().order_by('categorie')

    cweek = datetime.today().isocalendar()[1]

    weeks = []
    weeks.append(cweek)
    thisweekroutes = []
    lastweekroutes = []

    for rt in rts:
        if rt.date.isocalendar()[1] == cweek:
            thisweekroutes.append(rt)
        if rt.date.isocalendar()[1] == cweek - 1:
            lastweekroutes.append(rt)

    routes = []
    routes.append(thisweekroutes)
    routes.append(lastweekroutes)

    return render(request, 'routetest.html', {'routes': routes})
