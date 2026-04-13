from rest_framework import serializers
from .models import Provinces, Terminals



class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = '__all__'


class TerminalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminals
        fields = '__all__'