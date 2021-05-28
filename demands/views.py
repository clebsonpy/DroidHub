from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone as tz

from .models import Demands
from .serializers import DemandSerializer
from rest_framework import mixins, viewsets, status

from rest_framework.permissions import IsAuthenticated


class ListDemandsPermission(IsAuthenticated):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True

        if view.action == 'list':
            return True

        elif view.action == 'create':
            return request.user.id == request.data['user']

        elif view.action == 'retrieve':
            return view.get_object().user == request.user

        elif view.action == 'destroy':
            return view.get_object().user == request.user

        elif view.action == 'update' or view.action == 'partial_update':
            return view.get_object().user == request.user

        elif view.action == 'status':
            return view.get_object().user == request.user

        return False


# Create your views here.
class DemandsApiViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):

    serializer_class = DemandSerializer
    permission_classes = (ListDemandsPermission, )

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Demands.objects.all()

        return Demands.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        if 'status' in request.data.keys():
            return Response(data={'mensagem': 'Atualização de status é inválido!'},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        return super(DemandsApiViewSet, self).update(request=request, *args, **kwargs)

    @action(methods=['post'], detail=True)
    def status(self, request, pk=None):

        demand = self.get_object()
        data_status = request.data.get('status', None)

        demand.status = data_status

        if data_status == 'finish':
            demand.date_finish = tz.now().date()

        elif data_status == 'open':
            demand.date_finish = None

        else:
            return Response(data={'mensagem': 'Status inválido!'})

        demand.save(update_fields=['status', 'date_finish'])
        return Response(data=self.serializer_class(instance=demand).data, status=status.HTTP_202_ACCEPTED)

