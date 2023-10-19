from django.db import models

# Create your models here.

class ClassModel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=300)
    messages = models.TextField(max_length=200)
    
    
    
class ContactModel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    phonenumber = models.IntegerField()
    email = models.CharField(max_length=300)
    messages = models.TextField(max_length=200)