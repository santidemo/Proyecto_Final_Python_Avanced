from django.db import models
import datetime
from django_quill.fields import QuillField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = QuillField(
        default='<p></p>',  
        blank=True,
        null=True,
        
    )
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(default=datetime.date.today)
