from datetime import datetime

from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets

from .models import Route, RouteArchive, Category, GradeScale
from .serializers import RouteSerializer, RouteArchiveSerializer, CategorySerializer, GradeScaleSerializer


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


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view categories
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    http_method_names = ['get']


class GradeScaleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view grade scales
    """
    queryste = GradeScale.objects.all()
    serializer_class = GradeScaleSerializer
    http_method_names = ['get']


def testRouteList(request):
    rts = Route.objects.all().order_by('category')

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


def gradetest(request):
    if request.method == 'GET':
        return render(request, 'gradetest.html')
    elif request.method == 'POST':
        grade = request.POST['grade']
        grade = grade.lower()

        if grade == "*":
            grade_scales_filtered = GradeScale.objects.all()
        else:
            grade_scales_filtered = GradeScale.objects.filter(
                Q(french__iexact=grade)
            )
        if len(grade_scales_filtered) == 0:
            message = "Nothing found for <b>%s</b>" % grade
        else:
            message = "Searchresults for <b>%s</b>" % grade

        return render(request, 'gradetest.html', {'grades': grade_scales_filtered, 'message': message})
