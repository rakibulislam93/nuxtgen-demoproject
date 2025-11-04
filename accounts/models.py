from django.db import models
from django.contrib.auth.models import AbstractUser
from config import settings
# Create your models here.


USER_ROLE = (
    ('user','User'),
    ('staff','Staff'),
    ('admin','Admin')
)
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_role = models.CharField(choices=USER_ROLE,max_length=20,default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username } --- {self.email}'



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12,blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username