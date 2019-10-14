from rest_framework import serializers
from .models import Therapist

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = ('password', 'username', 'first_name', 'last_name', 'email','name', 'lastname', 'id_type','genre')