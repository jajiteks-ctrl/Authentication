from django.shortcuts import render

from rest_framework import generics,permissions
from django.contrib.auth.models import User
from app.models import Profile 
from app.serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Get or create the Profile associated with the User
        profile, created = Profile.objects.get_or_create(user=user)
        
       
        return Response({
            
            "username": user.username,
            "email": user.email,
            "bio": profile.bio,
            "profile_pic": profile.profile_pic.url if profile.profile_pic else None,  # Handling optional profile_pic
            "Designation": profile.Designation
        })
