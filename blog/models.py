from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products', blank=True)


    def __str__(self):
        return self.title
