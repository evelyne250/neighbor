from django.db import models
from django.contrib.auth.models import User

class NeighbourHood(models.Model):
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hood')
    location = models.CharField(max_length =30)
    occupants = models.IntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()


# class User(models.Model):
    