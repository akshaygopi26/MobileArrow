from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Mobile(models.Model):                #each class is going to be its own table in the DB
    Sno=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    base_color=models.CharField(max_length=100)
    processor=models.CharField(max_length=100)
    screen_size=models.CharField(max_length=100)
    ROM=models.CharField(max_length=100)
    RAM=models.CharField(max_length=100)
    display_size=models.CharField(max_length=100)
    num_rear_camera=models.CharField(max_length=100)
    num_front_camera=models.CharField(max_length=100)
    battery_capacity=models.CharField(max_length=100)
    ratings=models.CharField(max_length=100)
    num_of_ratings=models.CharField(max_length=100)
    sales_price=models.CharField(max_length=100)
    discount_percent=models.CharField(max_length=100)
    sales=models.CharField(max_length=100)
    units_sold=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.model}'