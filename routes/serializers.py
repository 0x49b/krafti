from rest_framework import serializers
from .models import Route, RouteArchive


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'url', 'grade', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'categorie']


class RouteArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'url', 'grade', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'categorie',
                  'archived']
