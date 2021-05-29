from django.db.models.fields import related
from django.shortcuts import render,redirect
from massage_app.models import *
from django.contrib import messages
import bcrypt

def index(request):
    if "user" in request.session:
        return redirect('/welcome')
    return render(request,"index.html")

def login(request): 
    if request.method == "POST":
        if request.POST["login_type"] == "register":
            errors = User.objects.Registration_validator(request.POST) 
            if email_check(request.POST):
                errors["used_email"] = "this email is already exist"
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                password = request.POST["password"]
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                creat_user(request.POST,pw_hash)
                reg_user = User.objects.last()
                if "user" not in request.session :
                    request.session["user"] = reg_user.id
                    request.session["name"] = reg_user.first_name
                    request.session["email"] = reg_user.email
                return redirect('/welcome')
        elif request.POST["login_type"] == "login":
            # if check_user(request.POST):
            #     # users = User.objects.filter(email=request.POST["email"])
            #     # user = users[0]
            #     return True
            user = User.objects.get(email = request.POST["email"])
            if "user" not in request.session:
                request.session["user"] = user.id
                request.session["name"] = user.first_name
                request.session["email"] = user.email
                return redirect('/welcome')
    elif request.method == "GET":
        return redirect("/")

def logout(request):
    request.session.clear()
    return render(request,"index.html")

def welcome(request):
    context = {
        "all_massages" : Massage.objects.all().order_by("-created_at"),
        "comments" : Comment.objects.all().order_by("-created_at"),
    }
    return render (request,"welcome.html",context)

def create_massage(request):
    current_user_id = request.session["user"]
    cuurent_user = User.objects.get(id = current_user_id )
    add_massage(request.POST,cuurent_user)
    # context = {
    #     "all_massages" : Massage.objects.all().order_by("created_at")
    # }
    return redirect('/welcome')

def create_comment(request):
    massage_id = int(request.POST["massage_id"])
    current_massage = Massage.objects.get(id = massage_id)
    current_user_id = request.session["user"]
    cuurent_user = User.objects.get(id = current_user_id )
    add_comment(request.POST,current_massage,cuurent_user)
    # context = {
    #     "comment": current_massage.comments.all().order_by("created_at")
    # }
    return redirect('/welcome')

def delete_massage(request):
    massage_id = int(request.POST["delete_massage"])
    del_massage(massage_id)
    return redirect('/welcome')

def delete_comment(request):
    comment_id = int(request.POST["delete_comment"])
    del_comment(comment_id)
    return redirect('/welcome')


