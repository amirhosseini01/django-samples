from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="login")
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles/profiles.html', context)

def LoginPage(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            print('err')
        
        user = authenticate(request=request, username= username, password = password)

        if(user is not None):
            login(request, user)
            return redirect('profiles')
        else:
            print('incorrect username or password')
    return render(request, 'login.html')

def Logout_User(request):
    logout(request)
    return redirect('login')