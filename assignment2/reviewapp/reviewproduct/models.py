from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    category_of_tech = (('Phone' , 'Phone'),
    ('CPU', 'CPU'),
    ('GPU', 'Graphics Card'),
    ('other', 'other'))
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    cost=models.DecimalField(max_digits=20, decimal_places=2)
    category=models.CharField(max_length=100, choices=category_of_tech)
    release=models.DateTimeField()
    description=models.TextField()
    photo_of_product=models.ImageField()

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    dateofbirth=models.DateTimeField()
    address=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    profile_picture= models.ImageField()
    def __str__(self):
        return str(self.user)

class Review(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,null=True, on_delete=models.CASCADE)
    product_rating=models.IntegerField(choices=list(zip(range(1,11), range(1,11))))
    review_text=models.TextField()
    Date_review=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.type
    def get_absolute_url(self):
        return reverse('review-review_text', kwargs={'pk': self.pk})


def __str__(self):
    return self.type
