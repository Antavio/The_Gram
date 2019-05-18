from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Image(models.Model):
    img_path = models.ImageField(upload_to = 'posts/',default="")
    img_title = models.CharField(max_length=60)
    img_caption = HTMLField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.img_title

    class Meta:
        ordering = ['-id']