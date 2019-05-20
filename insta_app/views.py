from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import ImageForm,ProfileEditorForm
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    return render(request,'registration/first_page.html')

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

@login_required(login_url='/accounts/login/')
def profile(request,username):
    users =request.user.id
    profile = Profile.objects.filter(user_profile=users).first()
    all_images = Image.objects.filter(insta_user=profile.user_profile).all()

    return render (request,"insta_app/profile.html",{"profile":profile,"all_images":all_images})

@login_required
def edit_profile_info(request,username):
    logged_user =request.user.id
    if request.method == 'POST':
        form = ProfileEditorForm(request.POST,request.FILES)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.user_profile = logged_user
            edit_profile.save()
            return redirect('home')
    else:
        form = ProfileEditorForm()

    return render(request,'profile/edit_profile.html',{'form':form})
