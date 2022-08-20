from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default='1')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=2000, )
    office_number = models.CharField(max_length=16,)
    cell_number = models.CharField(max_length=16,)
    role = models.CharField(max_length=54,)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} Profile"
