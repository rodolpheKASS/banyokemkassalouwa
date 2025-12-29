from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    published_date = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

