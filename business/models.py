from django.db import models
from django.contrib.auth.models import User


class BusinessModel(models.Model):
    ein = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=80, default='business')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    street = models.CharField(max_length=100)
    street_two = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.city}, {self.state}"

    class Meta:
        ordering = ['name']
