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

            return redirect("/bucketlist")
        
    return redirect("/bucketlist")

def login(request):
    user = User.objects.filter(
        email=request.POST["email"]
    )
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session["userid"] = logged_user.id
            return redirect("/bucketlist")
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

def get_all(request):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        context = {
            'plans': Plan.objects.all(),
        }
        return render(request, 'dashboard.html', context)

def add_plan(request):
    return render(request, 'add_plan.html')

def create_plan(request):
    if request.method == "POST":
        context= {
            'plan' : Plan.objects.create(name=request.POST['plan_name'], the_user=User.objects.get(id=request.session['userid']))
        }
        return render(request, 'add_activities.html', context)
    return redirect(request,'/created_plan')
          
def add_activity(request,plan_id):
    if request.method == "POST":
        Activity.objects.create(name=request.POST['activity'], the_plan=Plan.objects.get(id=plan_id))
    context = {
        'activities' : Activity.objects.filter(the_plan=Plan.objects.get(id=plan_id)),
        'plan' : Plan.objects.get(id=plan_id)
    }
    return render(request, 'a_plan.html', context)

def get_plan(request, id):
    if 'userid' in request.session:
        context = {
            'current_user':  User.objects.get(id=request.session['userid']),
            'plan' : Plan.objects.get(id=id),
        }
        return render(request, 'a_plan.html', context)
    else:
        return redirect('/')

def delete_plan(request, id):
    if 'userid' not in request.session:
        return redirect('/')
    plan_del = Plan.objects.get(id = id)
    plan_del.delete()
    return redirect('/dashboard')

def delete_activity(request, plan_id, act_id):    
    if 'userid' not in request.session:
        return redirect('/')
    act_del = Activity.objects.get(id = act_id)
    act_del.delete()
    return redirect(f'/get_plan/{plan_id}')
