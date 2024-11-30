from django.db import models
from django.utils import timezone

# Create your models here.

class Chai_Variety(model.Model):
    CHAI_TYPE_CHOICES =[
        ("ML",'MASALA'),
        ('EC', 'ELAICHI'),
        ('GR' , 'GINGER'),
        ('PL' , 'PLAIN'),
        ('VL' , 'VANILA'),
        ('TL' , 'TULSI'),
    ]

    name = models.CharField(max_length=20)
    imange = models.ImageField(upload_to="chai_Images/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1 , choices=CHAI_TYPE_CHOICES , default="ML")

    def __str__(self):
        return self.name