from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager For User Profiles"""

    def create_user(self, email, name="", password=None):
        """Create a new User Profile"""
        if not email:
            raise ValueError("User must have an email address")

        # normailize second half of email to lower case as it's not case sensitve
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email=email,password= password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):

    """Dtabase  model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


def generateToken(sender,instance,created,*args,**kwargs):
    print(created)
    if created:
        print("Token is being created")
        Token.objects.create(user=instance)
        
        
post_save.connect(generateToken, sender=settings.AUTH_USER_MODEL)
