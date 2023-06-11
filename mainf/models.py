from django.db import models

# Create your models here.

class BlogContent(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/', default=None, null=True)
    content = models.TextField()



class Comentbox(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    text=models.TextField(max_length=500)


