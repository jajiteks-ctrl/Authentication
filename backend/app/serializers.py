from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta :
        model = User
        fields = ['username','email','password']
        
    def validate_email(self, value):
        """
        🔒 Prevent duplicate emails
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data.get('email',"")
        )
        return user 
    
class ProfileSerialier(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio',' profile_pic','designation']
        
    
    
