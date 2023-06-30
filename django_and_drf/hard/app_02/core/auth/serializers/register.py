from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    """Registration serializer for request and user createion
    
    password -> 8 symbols
    """ 

    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'bio', 'avatar', 'email', 'username', 'first_name', 'last_name', 'apssword']

    def create(self, validated_data):
        """Use the create_user method to create a new user""" 

        return User.objects.create_user(**validated_data)

     