from django.db import models

# Create your models here.
class Travel(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()

class recent(models.Model):
    img=models.ImageField('image')
    head=models.CharField(max_length=120)
    des=models.TextField()