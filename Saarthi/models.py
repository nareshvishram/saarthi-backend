from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class User_Dtabase(models.Model):
    usr=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.usr

class URL(models.Model):
    usr = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    url=models.URLField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    date=models.DateField(default=datetime.now(),null=True,blank=True)

    def __str__(self):
        if self.url:
            return self.url
        else:
            return "None"
