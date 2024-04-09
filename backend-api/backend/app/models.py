from django.db import models

class Students(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=500)
    Lastname = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
