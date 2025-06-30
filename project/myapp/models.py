from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    contact=models.CharField()
    dob=models.CharField()
    education=models.CharField()
    gender=models.CharField()
    password=models.CharField()
    image=models.ImageField(upload_to='images/')
    file=models.FileField(upload_to='files/')
    discription=models.CharField(null=True)
  
class Query(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    query = models.TextField()