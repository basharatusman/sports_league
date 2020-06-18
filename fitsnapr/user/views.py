from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . forms import UserRegisterForm, UserUpdateForm, UserProfileForm, UserProfileUpdateForm
from django.http import HttpResponse
from . models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views import View


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


class ProfileView(View):
    user_update_form = UserUpdateForm
    profile_update_form = UserProfileUpdateForm
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        u_form = self.user_update_form(instance=request.user)
        p_form = self.profile_update_form(instance=request.user.userprofile)

        context = {'u_form': u_form, 'p_form': p_form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = self.user_update_form(request.POST, instance=request.user)
        p_form = self.profile_update_form(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

        context = {'u_form': u_form, 'p_form': p_form}

        return render(request, self.template_name, context)
