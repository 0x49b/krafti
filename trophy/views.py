from django.shortcuts import render
from .models import TrophyRoute, TrophyCategory
from rest_framework import viewsets
from .serializers import TrophyRouteSerializer, TrophyCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    selbstsicherung = TrophyRoute.objects.filter(category_id=3).order_by('number')
    return render(request, 'trophy/index.html', {'selbstsicherung': selbstsicherung})


class TrophyRouteViewSet(viewsets.ModelViewSet):
    serializer_class = TrophyRouteSerializer
    queryset = TrophyRoute.objects.all().order_by('number')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'number']


class TrophyCategoryViewSet(viewsets.ModelViewSet):
    queryset = TrophyCategory.objects.all()
    serializer_class = TrophyCategorySerializer
