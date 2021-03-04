from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=128, null=False, unique=True)
    content = models.TextField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)




