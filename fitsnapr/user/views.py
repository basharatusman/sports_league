from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import UserRegisterForm, UserUpdateForm, UserProfileForm, UserProfileUpdateForm
from django.http import HttpResponse
from . models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = UserProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            user.refresh_from_db()
            profile = UserProfileForm(request.POST, instance=user.userprofile)
            profile.full_clean()
            profile.save()
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = UserProfileForm()
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'user/register.html', context)


def home(request):
    return HttpResponse("Hello")


def profile(request):
    print(request.user.userprofile.profile_picture.url)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user)

    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'user/profile.html', context)
