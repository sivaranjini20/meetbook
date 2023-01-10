from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# profile is the table name
class Profile(models.Model):
    #cascade will remove the child object when the foreign object is deleted. 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to = 'profile', default='blank-profile-picture.png')
    location = models.TextField(max_length=100, blank=True)
    hobby= models.TextField(max_length=200,blank=True)
    education= models.TextField(max_length=200,blank=True) 
    
    def __str__(self):
        return self.user.username
