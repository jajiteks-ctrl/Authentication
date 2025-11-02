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
        
    

from app.models import Recipe
    
class ReceipeSerializer(serializers.ModelSerializer):
    author = serializers.CharField( read_only=True)
    class Meta :
        model = Recipe
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]
    
from app.models import Ratings

class RatingSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only =True)
    
    class Meta:
        model = Ratings
        fields = ['id','user','recipe','rating_value']
        read_only_fields = ['user']  # user is set automatically from request