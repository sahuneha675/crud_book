from django.db import models
from datetime import datetime,timedelta


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    password =  models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    subject = models.IntegerField()
    image = models.ImageField(upload_to="profile/", blank=True)

def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)