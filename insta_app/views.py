from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image

# Create your views here.
# @login_required(login_url='/accounts/login/')
def home(request):
    all_insta_images = Image.fetch_all_images()
    return render(request,'insta_app/index.html',{"all_insta_images":all_insta_images})
