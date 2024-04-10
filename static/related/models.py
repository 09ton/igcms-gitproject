from django.db import models
from datetime import datetime
# Create your models here.
class Related(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    held_in = models.CharField(max_length=100)
    held_on = models.DateTimeField()
    event_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    event_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    event_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    event_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    event_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
