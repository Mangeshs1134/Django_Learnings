from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Yummy(models.Model):
    user = models.ForeignKey(User , related_name='user', on_delete=models.CASCADE)
    text = models.TextField(max_length=235)
    # images = models.ImageField(upload_to='photos/', null=False) 
    # images = models.ImageField(upload_to='photos/', null=False) 
    images = models.ImageField(upload_to='yummy_images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
