from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm

# Create your views here.

def home(request):
    all_insta_images = Image.fetch_all_images()
    return render(request,'insta_app/index.html',{"all_insta_images":all_insta_images})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.insta_user = current_user
            user_img.save()
        return redirect('home')
    else:
        form = ImageForm()
    return render(request,"new_image.html",{"form":form})

