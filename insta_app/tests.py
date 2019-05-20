from django.test import TestCase
from .models import Image,Profile

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

