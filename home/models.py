from django.db import models

# Create your models here.

class Contact(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
