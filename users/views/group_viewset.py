from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from users.models import CustomGroup
from users.serializers import GroupSerializer

class GroupViewSet(ModelViewSet):
    queryset = CustomGroup.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes=[DjangoModelPermissions, IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if not request.user.has_perm('users.create_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.has_perm('users.update_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        if not request.user.has_perm('users.get_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=HTTP_403_FORBIDDEN)
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        if not request.user.has_perm('users.get_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.has_perm('users.destroy_group'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)