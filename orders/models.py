from django.db import models
from fooditem.models import FoodItem
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_time = models.TimeField(auto_now_add=True)
    table_no = models.IntegerField(default=1,unique=True)
    def __str__(self):
        """Return string representation of our user"""
        return str(self.table_no)
    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    fooditem = models.ManyToManyField(FoodItem,verbose_name="FOOD")
    quantity = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.order)
