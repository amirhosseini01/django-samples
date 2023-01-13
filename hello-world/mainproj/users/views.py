from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles/profiles.html', context)

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            print('err')
        
        user = authenticate(request, username, password)

        if(user is not None):
            login(request, user)
            return redirect('profiles')
    return render(request, 'users/login.html')