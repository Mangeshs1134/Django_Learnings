from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Yummy(models.Model):
    user = models.ForeignKey(User , related_name='user', on_delete=models.CASCADE)
    recipe_name = models.TextField(max_length=20 , null=True ,blank=True)
    text = models.TextField(max_length=235)
    likes = models.ManyToManyField(
        # settings.AUTH_USER_MODEL,
         User,
          blank=True, related_name='post_likes')
    images = models.ImageField(upload_to='yummy_images/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:5]}'

    @property
    def view_count(self):
        return RecipeLikes.objects.filter(recipe=self).count()
    
    @property
    def like_or_unlike( self):
        return RecipeLikes.objects.filter(user= self.user, recipe=self).exists()
        # return f"{self.user} - {self}"
    
    @property
    def isLiked(self):

        ret = RecipeLikes.objects.filter( recipe=self, isLikedPost=True)
        # return f'{ret}'
        return RecipeLikes.objects.filter( recipe=self, isLikedPost=True)


class RecipeLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Yummy, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    isLikedPost = models.BooleanField(default=True)

    class Meta :
        unique_together = ('user', 'recipe')
    
    def __str__(self):
        # return f'{self.user.username} likes - {self.recipe.recipe_name}
        return self.user.username
