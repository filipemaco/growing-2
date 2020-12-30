from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Objectives


class ObjectivesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title', 'subtitle', 'importance', 'updated_at', 'created_at'
        )
        model = Objectives
