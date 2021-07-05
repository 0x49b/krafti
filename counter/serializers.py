from rest_framework import serializers
from .models import Visits


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ['id', 'current_loggedin', 'current_free', 'added', 'url']
