from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_pictures/',default="")
    user_bio = models.CharField(max_length=200,blank=True)
    user_profile = models.IntegerField(default=0)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls,name):
        profile = Profile.objects.filter(user_profile__username__icontains = name)
        return profile

    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.get(user_profile=id)
        return profile

    @classmethod
    def filter_profile_by_id(cls,id):
        profile = Profile.objects.filter(user_profile=id).first()
        return profile

class Image(models.Model):
    img_path = models.ImageField(upload_to = 'posts/',default="")
    img_title = models.CharField(max_length=60)
    img_caption = HTMLField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    insta_user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.img_title

    class Meta:
        ordering = ['-id']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_single_image(cls,id):
        single_image = Image.objects.get(pk=id)
        return single_image

    @classmethod
    def fetch_all_images(cls):
        all_images = Image.objects.all()
        return all_images