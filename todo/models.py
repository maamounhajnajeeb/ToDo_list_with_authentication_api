from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Tasks(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=512)
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    