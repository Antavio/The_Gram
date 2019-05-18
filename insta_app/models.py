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

    def save_image(self):
        self.save()

    @classmethod
    def get_single_image(cls,id):
        single_image = Image.objects.get(pk=id)
        return single_image

    @classmethod
    def fetch_all_images(cls):
        all_images = Image.objects.all()
        return all_images