from rest_framework import serializers
from .models import GameSession,Performance,TherapySession,Minigame

class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'


class TherapySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapySession
        fields = '__all__'

class MinigameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minigame
        fields = '__all__'