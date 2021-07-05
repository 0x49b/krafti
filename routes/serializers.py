from rest_framework import serializers
from .models import Route, RouteArchive, Category, GradeScale


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'uuid', 'grade', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'category', 'slug',
                  'archived', 'url']


class RouteArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteArchive
        fields = ['uuid', 'url', 'grd', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'category', 'slug',
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


class AllRoutesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=False, many=False)
    grade = GradeScaleSerializer(read_only=False, many=False)

    class Meta:
        model = Route
        fields = ['id', 'uuid', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'grade', 'category', 'slug',
                  'archived', 'url']
