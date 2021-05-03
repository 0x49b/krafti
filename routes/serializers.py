from rest_framework import serializers

from .models import Route, RouteArchive, Category, GradeScale


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'url', 'grade', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'category', 'slug']


class RouteArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteArchive
        fields = ['id', 'url', 'grade', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'category', 'slug',
                  'archived']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'slug']


class GradeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScale
        fields = ['id', 'url', 'yds', 'british_tech', 'british_adj', 'french', 'uiaa', 'australia', 'saxon',
                  'scandinavia', 'brasil', 'fontainebleu']
