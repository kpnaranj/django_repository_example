from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional classes 
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    