from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 


from django.utils import timezone

# Create your models here.

class Resume(models.Model):


    name = models.CharField(max_length=200,null=True)   
    address1 = models.CharField(max_length=200,blank=True,null=True)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    obj = models.TextField(max_length=400,blank=True,null=True) 

    image = models.FileField(upload_to='')


    school = models.CharField(max_length=200,blank=True,null=True)
    UG = models.CharField(max_length=200,blank=True,null=True)
    PG = models.CharField(max_length=200,blank=True,null=True)
    
    skills = models.CharField(max_length=200,blank=True,null=True)
    
    cell = models.IntegerField()

    email = models.EmailField(max_length=70,blank=True,null=True)

    expfrom = models.DateTimeField(
            blank=True, null=True)
    expto = models.DateTimeField(
            blank=True, null=True)
    expone = models.CharField(max_length=200,blank=True,null=True)
   
    exptwo = models.CharField(max_length=200,blank=True,null=True)





    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
