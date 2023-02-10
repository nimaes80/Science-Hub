from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models

# Create your models here.



class UserManager(AbstractUserManager):


    pass

class User(AbstractUser):


    objects = UserManager()
