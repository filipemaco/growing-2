from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import ObjectiveViewSet

router = SimpleRouter()
router.register('', ObjectiveViewSet, basename='objectives')

urlpatterns = router.urls
