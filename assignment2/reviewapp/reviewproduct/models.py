from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class product(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    cost=models.DecimalField(max_digits=20, decimal_places=2)
    category=models.CharField(max_length=100)
    release=models.DateTimeField()
    description=models.TextField()
    photo_of_product=models.ImageField()

class profile(models.Model):
    name=models.CharField(max_length=100)
    dateofbirth=models.DateTimeField()
    address=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    profile_picture= models.ImageField()

class review(models.Model):
    author=models.CharField(max_length=100)
    product_rating=models.IntegerField(choices=list(zip(range(1,11), range(1,11))))
    review_text=models.TextField()
    Date_review=models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.type