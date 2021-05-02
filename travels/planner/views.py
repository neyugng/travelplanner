from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re

def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        
        if User.objects.filter(email = request.POST["email"]):
            messages.error(request, "Email is already registered and can be used to login!")
            return redirect("/")
            
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        
        else:
            password = request.POST["password"]
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name = request.POST["first_name"],
                last_name = request.POST["last_name"],
                email = request.POST["email"],
                password = password_hash,
            )
            request.session["userid"] = new_user.id

            return redirect("/")
        
    return redirect("/")

def login(request):
    user = User.objects.filter(
        email=request.POST["email"]
    )
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session["userid"] = logged_user.id
            return redirect("/")
        else:
            messages.error(request, "We don't recognize that email address and/or password.")
    else:
        messages.error(request, "We don't recognize that email address and/or password.")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect('/')

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
