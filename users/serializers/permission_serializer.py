from rest_framework import serializers

from users.models import CustomPermission
        
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = "__all__"