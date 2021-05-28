from django.shortcuts import render,redirect
from login_app.models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def login(request):
    errors = User.objects.Registration_validator(request.POST)  
    if request.method == "POST":
        if request.POST["login_type"] == "register":
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            # if email_check(request.POST):
            #     return redirect("/")
            else:
                password = request.POST["password"]
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                creat_user(request.POST,pw_hash)
                redirect("/")
        if request.POST["login_type"] == "login":
            if check_user(request.POST):
                users = User.objects.filter(email=request.POST["email"])
                user = users[0]
                if "user" not in request.session:
                    request.session["user"] = user.first_name
                    request.session["email"] = user.email
                    return render (request,"welcome.html")
    # if request.method == "GET":
    #     return redirect("/")