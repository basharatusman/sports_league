from django.urls import path
from .views import register, home, ProfileView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', register, name='register-view'),
    path('profile/', ProfileView.as_view(), name='profile-view'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', home, name='home')
] 
