from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            email= validated_data['email']
        )
        return user