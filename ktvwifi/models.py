from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.utils import timezone



# Create your models here.
class InternetPlans(models.Model):
    speed = models.CharField(max_length=200 , null=True)
    price = models.IntegerField(null=True)
    validity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.speed + ' Mbps ' + str(self.price) + ' Price ' + str(self.validity) + ' Days '

class Contact(models.Model):
    STATUS_CHOICES = (
    ('p', 'Pending'),
    ('c', 'Completed'),
    ) 
    name = models.CharField(max_length=50 )
    phone = models.CharField(max_length=20 , null=True)
    email = models.CharField(max_length=50 , null=True)
    title = models.CharField(max_length=100 , null=True)
    message = models.TextField(null=True)
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES, default='p')
    response = models.TextField(null=True)
    ip = models.CharField(max_length=50 , null=True )
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name  

class Faq(models.Model):
    title = models.CharField(max_length=200 , null=True , blank=True)
    solution = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "%s" % self.title 

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20 , null=True , blank=True)
    dp = models.ImageField(null=True , blank=True)
    address = models.TextField(null=True)
    ip =  models.CharField(max_length=50 , null=True , blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "%s" % self.user  

class Complaint(models.Model):
    STATUS_CHOICES = (
    ('p', 'Pending'),
    ('o', 'Out for complaint'),
    ('c', 'Completed'),
    ) 
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=200 , null=True , blank=True)
    message = models.TextField(null=True)
    image = models.ImageField(null=True , blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    solution = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "%s" % self.user  

