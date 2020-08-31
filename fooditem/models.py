from django.db import models

# Create your models here.
class FoodItem(models.Model):
    food_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=7,decimal_places=2)
    
    item_category = models.CharField(max_length=255)
    def __str__(self):
        """Return string representation of our user"""
        return self.name