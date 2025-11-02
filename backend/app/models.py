from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null = True, blank = True)
    profile_pic= models.ImageField(upload_to = "media/", null = True, blank = True)
    Designation = models.CharField(null = True, blank = True,  default="Student")

    def __str__(self):
        return self.user.username    


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100,  blank = True)
    description = models.TextField( blank = True)
    image = models.ImageField(null = True, blank = True, upload_to="recipe/")
    ingredients = models.TextField()
    steps = models.TextField()
    tags = models.CharField(max_length = 100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    average_rating = models.FloatField(default = 0.0)
    
    def __str__(self):
        return self.title or "untitled Receipe"
    
    
class Ratings(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating_value = models.PositiveIntegerField(default = 1)
    
    class Meta:
        unique_together = ('recipe','user') # prevent duplicates
    
    def __str__(self):
       return f" {self.user.username} rated {self.recipe.title} and  {self.rating_value}"
    
  
    
   
   
    
   
    
    
  