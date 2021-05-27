from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import CustomTokenObtainPairView, UserViewSet, RegisterView

# app_name = 'accounts'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/register/', RegisterView.as_view(), name='register'),
    path('v1/', include(router.urls)),
    path('', include('rest_framework.urls')),
]
