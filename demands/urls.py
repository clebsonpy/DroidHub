from django.urls import path, include
from rest_framework import routers

from .views import DemandsApiViewSet

app_name = 'demands'

router = routers.SimpleRouter()
router.register('', DemandsApiViewSet, basename='demands')

urlpatterns = [
    path('', include(router.urls))
]
