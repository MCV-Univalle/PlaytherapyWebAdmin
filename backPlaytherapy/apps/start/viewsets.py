from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from .models import GameSession,Performance,TherapySession,Minigame
from .serializer import GameSessionSerializer, PerformanceSerializer, TherapySessionSerializer, MinigameSerializer
from rest_framework import viewsets

# Create your views here.
class GameSessionViewSet(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class TherapySessionViewSet(viewsets.ModelViewSet):
    queryset = TherapySession.objects.all()
    serializer_class = TherapySessionSerializer

class MinigameViewSet(viewsets.ModelViewSet):
    queryset = Minigame.objects.all()
    serializer_class = MinigameSerializer