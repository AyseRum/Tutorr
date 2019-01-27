from django.db import models
import datetime
# Create your models here.
class User(models.Model):
     objects = models.Manager()
     firstName = models.CharField(max_length = 200)
     lastName = models.CharField(max_length = 200)
     DOB = models.DateField(("Date"), default=datetime.date.today)
     profilePic = models.ImageField(upload_to='images/')
     school = models.CharField(max_length = 200)
     phoneNum = models.IntegerField()
     email = models.EmailField(max_length = 250)
     rating = models.IntegerField(default = "0")