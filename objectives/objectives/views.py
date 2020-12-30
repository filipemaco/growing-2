from rest_framework import viewsets

from .models import Objectives

from .serializers import ObjectivesSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objectives.objects.all()
    serializer_class = ObjectivesSerializer
