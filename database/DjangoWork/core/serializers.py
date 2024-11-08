from rest_framework import serializers
from .models import User, TrafficLaw, Violation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TrafficLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficLaw
        fields = '__all__'

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'