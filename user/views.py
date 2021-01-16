from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import gettext as _

from user.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'list': UserSerializer,
        'create': UserCreateSerializer,
        'update': UserUpdateSerializer
    }

    def get_permissions(self):
        if self.action in ('update', 'destroy', 'list', 'retrieve'):
            permission_classes = [IsAdminUser]
        elif self.action in 'create':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, UserSerializer)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        if self.request.data.get('password'):
            instance.set_password(self.request.data.get('password'))
            instance.save()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return Response(UserSerializer(self.request.user).data)
