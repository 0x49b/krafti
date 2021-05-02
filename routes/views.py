from django.shortcuts import render
from rest_framework.response import Response

from .models import Route, RouteArchive
from datetime import datetime
from rest_framework import viewsets, generics
from .serializers import RouteSerializer, RouteArchiveSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view routes
    """
    queryset = Route.objects.all().order_by('-date')
    serializer_class = RouteSerializer
    http_method_names = ['get']


class RouteArchiveViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view routearchive
    """
    queryset = RouteArchive.objects.all().order_by('-archived')
    serializer_class = RouteArchiveSerializer
    http_method_names = ['get']


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
