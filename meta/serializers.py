from rest_framework import serializers
from .models import OpeningHours


class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ['id', 'day', 'open_from', 'close_at', 'special']
