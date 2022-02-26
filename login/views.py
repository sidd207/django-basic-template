from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Function to handle login request.
def login(request):
    if request.method == 'POST':
        
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/code')
        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('/')
    else:    
        return render(request, 'login.html')
    

#Function to handle logout request.
def logout(request):
    auth.logout(request)
    return redirect('/')