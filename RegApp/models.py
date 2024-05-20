from django.db import models

class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    index = models.CharField(max_length=20)
    password = models.CharField(max_length=80)