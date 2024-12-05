from django.db import models

class Category(models.Model):


  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name
   
class Coupon(models.Model):

  code = models.CharField(max_length=255, unique=True)
  discount_rate = models.FloatField()

class Product(models.Model):

  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.IntegerField()
  category = models.ForeignKey(Category,  on_delete=models.CASCADE)
  discount_rate = models.FloatField()
  coupon_applicable = models.BooleanField()
 

