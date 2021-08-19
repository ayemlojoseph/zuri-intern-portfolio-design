from django.db import models
from django_countries.fields import CountryField

# Create your models here.



class Contact (models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField(max_length=255, null=True, blank=True)
    country = CountryField()

    def __str__(self):
        return str(self.email)

