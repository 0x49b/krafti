from rest_framework import serializers
from .models import Route, Category, GradeScale


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'slug']


class GradeScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeScale
        fields = ['id', 'url', 'yds', 'british_tech', 'british_adj', 'french', 'uiaa', 'australia', 'saxon',
                  'scandinavia', 'brasil', 'fontainebleu']


class RoutesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=False, many=False)
    grade = GradeScaleSerializer(read_only=False, many=False)

    class Meta:
        model = Route
        fields = ['id', 'uuid', 'color', 'name', 'setter', 'date', 'length', 'route_num', 'grade', 'category', 'slug',
                  'archived', 'url']
