from django.shortcuts import render, redirect

from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
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
            messages.error(request=request, message= 'an unhandled error occurred! call support')
        
        user = authenticate(request=request, username= username, password = password)

        if(user is not None):
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request=request, message= 'incorrect username or password')
    return render(request, 'login.html')

def Logout_User(request):
    logout(request)
    return redirect('login')

def RegisterUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # give instance without saving in database
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user was created successfully')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'please complete form with correct information')

    context = {'form': form}
    return render(request, 'register.html', context= context)