from rest_framework import routers
from .viewsets import GameSessionViewSet,PerformanceViewSet,TherapySessionViewSet,MinigameViewSet

router = routers.SimpleRouter()
router.register('gamesession', GameSessionViewSet)
router.register('performance', PerformanceViewSet)
router.register('therapySession', TherapySessionViewSet)
router.register('minigame', MinigameViewSet)

urlpatterns = router.urls
