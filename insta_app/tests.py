from django.test import TestCase
from .models import Image,Profile,User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_profile = Profile(id=1,user_bio='Test Bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_instance(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_image(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    def test_find_profile_by_id(self):
        profiles = Profile.filter_profile_by_id(self.new_profile.id)
        self.assertTrue(profiles == self.new_profile)

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = Profile(user_bio='Test Bio')
        self.new_image = Image(id=2,img_title="Test Title",img_caption='Test Caption',date_posted='2017-02-01',insta_user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_instance(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_profile(self):
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_find_image_by_id(self):
        images = Image.get_single_image(self.new_image.id)
        self.assertTrue(images == self.new_image)