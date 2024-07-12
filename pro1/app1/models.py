from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    mobile_no =models.BigIntegerField()
    gender = models.CharField(max_length=40)
