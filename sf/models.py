from random import choices
from django.db import models
from traitlets import default

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40,default=None)
    last_name = models.CharField(max_length=40,default=None)
    username = models.CharField(max_length=40)
    profile_picture=models.ImageField(upload_to="profile_images", blank=True)
    email = models.EmailField(max_length=70)
    password = models.CharField( max_length=50)
    confirm_password= models.CharField( max_length=50,default=None)
    CATEGORIES=(
        ('COM', 'Combat'),
        ('CRA', 'Crafting'),
    )
    category = models.BooleanField( choices=CATEGORIES)


# class Address(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60, default="Miami")
#     state = models.CharField(max_length=30, default="Florida")
#     zipcode = models.CharField(max_length=5, default="33165")
#     country = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = 'Address'
#         verbose_name_plural = 'Address'

#     def __str__(self):
#         return self.name
    
