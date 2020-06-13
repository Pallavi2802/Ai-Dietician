from django.db import models

# Create your models here.
class AddUser(models.Model):
    Name=models.CharField(max_length=50,default=None)
    Email = models.EmailField(unique=True)
    Username = models.CharField(max_length=50,unique=True)
    Password = models.CharField(max_length=40)
   # Profile = models.ImageField()
   # Active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.Email)

class Diet(models.Model):
    users = models.CharField(max_length=50, null=True)
    age  = models.IntegerField( null=True)
    height = models.IntegerField( null=True)
    weight = models.IntegerField( null=True)
    gender = models.CharField(max_length=50, null=True)
    activity = models.CharField(max_length=50, null=True)
    
    
    


class BodyMassIndex(models.Model):
   BMI = models.CharField(max_length=50,null=True)

class Calories(models.Model):
   defg = models.CharField(max_length=50,null=True)