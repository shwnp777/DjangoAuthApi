from django.db import models
from django.contrib.auth.models import User
from business.models import BusinessModel


class ClientModel(models.Model):
    business = models.ForeignKey(BusinessModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_since = models.DateField()
    office_phone = models.CharField(max_length=30)
    cell_phone = models.CharField(max_length=30)
    points = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}, on {self.created_at}"

    class Meta:
        ordering = ['created_at']


class NotesModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s note, to {self.client}, on {self.created_at}"

    class Meta:
        ordering = ['created_at']
