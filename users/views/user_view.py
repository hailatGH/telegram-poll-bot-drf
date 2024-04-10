from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from users.serializers import UserSerializer

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('users.get_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        queryset = CustomUser.objects.all().order_by('created_at')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('users.create_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(guid=pk)
        except CustomUser.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not request.user.has_perm('users.get_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not request.user.has_perm('users.update_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not request.user.has_perm('users.update_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        user = self.get_object(pk)
        if not request.user.has_perm('users.destroy_user'):
            return Response({'message': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
