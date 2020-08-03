'''

what we have learned :
   1) How to use local storage
   2) How to integrate javascript and django code
   3) How to Post form data directly to the database
   4) How to use Jquery to handle front end user actions.
   
'''

from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_field = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/', max_length=100)

    def __str__(self):
        return self.title


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    zipcode = models.CharField(max_length=1000)
    total = models.CharField(max_length=200)
