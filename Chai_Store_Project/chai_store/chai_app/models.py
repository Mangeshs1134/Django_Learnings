from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
    type = models.CharField(max_length=3 , choices=CHAI_TYPE_CHOICES , default="ML")
    # description = models.TextField(default="Great Tea")

    def __str__(self):
        return self.name
    
class Chai_Reviews(models.Model):
    chai = models.ForeignKey(Chai_Variety , related_name= 'reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User , related_name='user', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.User.username} reviews for {self.chai.name}"

class Stores(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField( max_length=50)
    avail = models.ManyToManyField(Chai_Variety , related_name= 'avail_varieties' )

    def get(self):
        return ", ".join([str(p) for p in self.avail.all()])

    def __str__(self):
        return self.name

class Certificates(models.Model):
    certificate_num = models.IntegerField()
    issue_date = models.DateTimeField(default=None)
    exp_date = models.DateTimeField(default=None)
    chai = models.OneToOneField(Chai_Variety, on_delete=models.CASCADE , related_name='certificates')

    def __str__(self):
        return f'Certificate for {self.chai.name}'

