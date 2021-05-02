from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re

def index(request):
    return render(request, 'login.html')

#TODO need register function
#TODO need login check function
#TODO save the logged user in session
#TODO need log out function

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id),
    }
    return render(request, 'account.html', context)

def update(request, user_id):
    if request.method == 'POST':
        errors = {}
        if User.objects.filter(email = request.POST["email"]):
            messages.error(request, "Email is already registered.")
            return redirect(f"/myaccount/{user_id}")
        
        if len(request.POST["first_name"]) == 0:
            messages.error(request, "First name cannot be blank.")
            return redirect(f"/myaccount/{user_id}")
        
        if len(request.POST["last_name"]) == 0:
            messages.error(request, "last name cannot be blank.")
            return redirect(f"/myaccount/{user_id}")
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(request.POST['email']):
            errors["email"] = "Invalid email address."
            return redirect(f"/myaccount/{user_id}")
            
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        
        update_user = User.objects.get(id=user_id)
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.save()
    return redirect(f"/myaccount/{user_id}")


def add_plan(request):
    if request.method == "POST":
        #Plan.objects.create(name=request.POST['plan name'], the_user=User.objects.get(id=request.session['user_id']))
        pass

def get_plan(request, id):
    '''
    if 'user_id' in request.session:
        context = {
            'current_user':  User.objects.get(id=request.session['user_id']),
            'plan' : Plan.objects.get(id=id),
        }
        return render(request, 'a_plan.html', context)
    else:
        return redirect('/')
    '''
    pass    

def update_plan(request):
    '''
    
    '''
    pass
