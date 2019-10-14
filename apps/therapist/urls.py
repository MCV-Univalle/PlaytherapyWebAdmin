from rest_framework import routers
from .viewsets import TherapistViewSet

router = routers.SimpleRouter()
router.register('therapist', TherapistViewSet)

urlpatterns = router.urls
