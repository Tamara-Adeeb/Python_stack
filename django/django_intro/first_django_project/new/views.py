from django.shortcuts import render,redirect,HttpResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,number):
    
    return HttpResponse(f"<h1>placeholder to display blog number: {number} </h1>" )

def edit(requst,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blogs")

def Json(request):
    context = {
        "title":"My First blog",
        "content" : "Lorem, ipsum dolor sit amet consectetur adipisicing elit"
    }
    return(context)
