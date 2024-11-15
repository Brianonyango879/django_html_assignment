from wsgiref.validate import validator

from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=500,validators=[MinLengthValidator(100)])

    def __str__(self):
        return self.name