
from django.shortcuts import render,redirect
from fav_app.models import *
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
            errors = User.objects.login_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
            else:
                user = User.objects.get(email = request.POST["email"])
                if "user" not in request.session:
                    request.session["user"] = user.id
                    request.session["name"] = user.first_name
                    request.session["email"] = user.email
                    return redirect('/welcome')
    # elif request.method == "GET":
    #     return redirect("/")
    return redirect("/")

def welcome(request):
    if "user" not in request.session:
        return redirect("/")
    current_user = User.objects.get(id=request.session["user"])
    context = {
        "all_books": Book.objects.all(),
        "current_user": User.objects.get(id=request.session["user"]),
        "fav_book": current_user.liked_books.all()
    }
    return render (request,"welcome.html",context)

def logout(request):
    request.session.clear()
    return render(request,"index.html")

def add_fav_book(request):
    user = User.objects.get(id=request.session["user"])
    user_id = user.id
    create_fav_book(request.POST,user_id)
    return redirect('/welcome')

def display_book(request,id):
    current_book = Book.objects.get(id=id)
    context = {
        "book": Book.objects.get(id=id),
        "current_user": User.objects.get(id=request.session["user"]),
        "fav_book": current_book.users_who_like.all()
    }
    return render(request,"display_book.html",context)

def update_book(request,id):
    print(request.POST["desc"])
    update_book_desc(request.POST,id)
    return redirect('books/'+str(id))

def delete_book(request,id):
    delete_allBook(id)
    return redirect('books/'+str(id))

def un_favorit_book(request,id,uid):
    un_favorit(id,uid)
    return redirect('books/'+str(id))

def fav_book(request,id,uid):
    user_fav_book(id,uid)
    return redirect('books/'+str(id))


