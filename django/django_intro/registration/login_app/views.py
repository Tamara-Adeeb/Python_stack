from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
from login_app.models import *
import  bcrypt

def index(request):
    return render(request,"index.html")

def login(request):
    errors = Users.objects.registration_validater(request.POST)
    if request.method == "POST":
        if request.POST["login_type"] == "registration":
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                register(request.POST,pw_hash )
                return redirect("/")
        if request.POST["login_type"] == "login":
            if check_user(request.POST):
                users = Users.objects.filter(email=request.POST["email"])
                user = users[0]
                context = {
                    "name" :  user.first_name , #f"{user.first_name} {user.last_name}"
                    "password":user.password
                }
                return render (request,"welcome.html",context)
            else:
                return redirect("/")




# def login(request):
#     if request.method == "POST":
#         if request.POST["login_type"] == "login":
#             if models.check_user(request.POST["name"], request.POST["password"]):
#                 request.session["user_name"] = request.POST["name"]
#                 return render(request,"welcome.html")
#             else:
#                 return redirect("/")
#         if request.POST["login_type"] == "registration":
#             models.register(request.POST["name"], request.POST["password"])
#     return redirect("/")