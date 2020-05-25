from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
            User,
            on_delete = models.CASCADE
             )
    contactno = models.CharField(max_length=10, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/user/profile_pic/', blank=True, null=True)
    ROLETYPE = (
        ('B','Buyer'),
        ('M','Merchant')
    )
    role = models.CharField(max_length=1,choices=ROLETYPE)
    country = models.CharField(max_length=120)

    def __str__(self):
        return user.username

#class MerchantProfile(models.Model):





class Industry(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Skill(models.Model):
    myindustry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    myskill = models.CharField(max_length= 100)
    def __str__(self):
        return self.myskill




class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category =  models.ForeignKey(Industry, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)
    productname = models.CharField(max_length=100)
    description = models.TextField()
    technical = models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.FileField(upload_to='media/product/mainfile/')
    productpic = models.ImageField(upload_to='media/product/displaypic/')
    image1 = models.ImageField(upload_to='media/product/productimages/')
    image2 = models.ImageField(upload_to='media/product/productimages/')
    image3 = models.ImageField(upload_to='media/product/productimages/')
    image4 = models.ImageField(upload_to='media/product/productimages/')