from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, RegisterSerializer
from .models import User


class ListUserPermission(IsAuthenticated):

    def has_permission(self, request, view):

        if view.action == 'list':
            return request.user.is_superuser

        elif view.action == 'retrieve':
            if request.user.is_superuser:
                return True

            return request.user == view.get_object()

        return False


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = ()


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (ListUserPermission,)


class RegisterView(GenericAPIView):
    """
    An api to register new users
    """
    serializer_class = RegisterSerializer
    permission_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
