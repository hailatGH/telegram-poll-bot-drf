from django.contrib.auth.models import Permission

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.serializers import PermissionSerializer

class PermissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('auth.view_permission'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        queryset = Permission.objects.all().order_by('id')
        serializer = PermissionSerializer(queryset, many=True)
        return Response(serializer.data)