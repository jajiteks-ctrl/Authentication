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

from app.models import Recipe
from app.serializers import ReceipeSerializer

class PostReceipeView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class GetallReceipeView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class GetSingleReceipeView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
class EditRecipe(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
class DeleteRecipe(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = ReceipeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
    
from app.serializers import RatingSerializers
from app.models import Ratings

class RatingView(generics.CreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [IsAuthenticated]
       
    def perform_create(self, serializer):
        serializer.save(user = self.request.user )
        
        
class GetallRatings(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [IsAuthenticated]
    
class GetSingleRatings(generics.RetrieveAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    

    
    