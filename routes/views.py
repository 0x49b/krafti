from rest_framework import viewsets
from .models import Route, Category, GradeScale
from .serializers import CategorySerializer, GradeScaleSerializer, RoutesSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view routes
    """
    queryset = Route.objects.filter(archived=False).order_by('-date')
    serializer_class = RoutesSerializer
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
    queryset = GradeScale.objects.all().order_by('french')
    serializer_class = GradeScaleSerializer
    http_method_names = ['get']


class CurrentGradesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint top get only current Grades in not archived routes (Can be used for filters)
    """
    rtes = Route.objects.filter(archived=False)
    grd = []
    for rt in rtes:

        if rt.grade.french not in grd:
            grd.append(rt.grade.french)

    queryset = GradeScale.objects.filter(french__in=grd).order_by("french")
    serializer_class = GradeScaleSerializer
