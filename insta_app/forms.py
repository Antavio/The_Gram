from django import forms
from .models import Image,Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['insta_user','date_posted']

class ProfileEditorForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_profile']
