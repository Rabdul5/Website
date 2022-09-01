from django.db import models

# Create your models here.
class News(models.Model):
    header = models.TextField()
    creators = models.CharField(max_length=16)
    tag =models.TextField()
    content = models.TextField()
    image = models.ImageField()
    data_post = models.DateTimeField(auto_now=True)