from typing import ContextManager
from django.shortcuts import redirect, render
# from . import models 
from books_authors_app.models import *

def book(request):
    context = {
        "Book" : Books.objects.all()
    }
    return render(request,"book.html",context)

def book_data(request):
    add_book(request.POST["title"],request.POST["desc"])
    return redirect('/')

def book_show(request,id):
    b = Books.objects.get(id=id)
    request.session["Book_id"] = id
    context = {
        "My_book": b,
        "auth": b.author.all(),
        "All_Authors":Authors.objects.all()
    }
    return render(request,"book_info.html",context)

def author(request):
    context = {
        "Author" : Authors.objects.all()
    }
    return render(request,"author.html",context)

def author_data(request):
    add_author(request.POST["fname"],request.POST["lname"],request.POST["note"])
    return redirect('/authors')

def author_show(request,id):
    request.session["id"] = id
    k = Authors.objects.get(id=id)
    context = {
        "My_author": k,
        "books" : k.Books.all(),
        "All_Book":Books.objects.all()
    }
    return render(request,"author_info.html",context)

def select_book(request):
    this_author = Authors.objects.get(id = request.session["id"])
    Bo = request.POST["select_book"]
    create_book(this_author,Bo)
    return redirect("authors/"+str(request.session["id"]))
def select_auth(request):
    this_book = Books.objects.get(id=request.session["Book_id"])
    selected_book = request.POST["select_auther"]
    create_author(this_book ,selected_book)
    return redirect("books/"+str(request.session["Book_id"]))





