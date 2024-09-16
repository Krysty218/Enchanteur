from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html',{})
 
from django.contrib.auth import get_backends

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('events')  # Redirect to events page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
