from rest_framework import serializers

from users.models import CustomGroup
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        fields = "__all__"
        