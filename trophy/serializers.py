from rest_framework import serializers
from .models import TrophyRoute, TrophyCategory
from routes.serializers import RoutesSerializer


class TrophyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrophyCategory
        fields = ['id', 'name', 'color']


class TrophyRouteSerializer(serializers.ModelSerializer):
    category = TrophyCategorySerializer(read_only=True, many=False)
    route = RoutesSerializer(read_only=True, many=False)

    class Meta:
        model = TrophyRoute
        fields = ['id', 'number', 'category', 'route', 'done']
