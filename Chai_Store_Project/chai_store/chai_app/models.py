from django.db import models
from django.utils import timezone

# Create your models here.

class Chai_Variety(models.Model):
    CHAI_TYPE_CHOICES =[
        ("ML",'MASALA'),
        ('EC', 'ELAICHI'),
        ('GR' , 'GINGER'),
        ('PL' , 'PLAIN'),
        ('VL' , 'VANILA'),
        ('TL' , 'TULSI'),
    ]

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="chai_images/")
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='Great Tea')
    type = models.CharField(max_length=5 , choices=CHAI_TYPE_CHOICES , default="ML")
    # description = models.TextField(default="Great Tea")

    def __str__(self):
        return self.name
    
class Chai_Reviews(models.Model):
    chai = models.ForeignKey(Chai_Variety , related_name="Chai_Reviews", on_delete=models.CASCADE)
    user = models.ForeignKey( super, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.User.username} reviews for {self.chai.name}"