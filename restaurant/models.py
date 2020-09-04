from django.db import models

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key = True)
    restaurant_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    picture = models.ImageField(null=True,blank=True,upload_to="restaurant_picture")

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True,)
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE)