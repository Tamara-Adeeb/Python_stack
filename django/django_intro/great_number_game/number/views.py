from django.shortcuts import redirect, render
import random 	                # import the random module

def random(request):
    if "random" not in request.session:
        request.session["random"] = 0
    request.session["random"] = request.POST["user_number"]
    return(request, "index.html")

def check(request):
    context = {
        "random": request.session["random"],
        "number": request.POST["user_number"]
    }
    if request.POST["user_number"] > request.session["random"]:
        request.session["result"] = 0
    if request.POST["user_number"] == request.session["random"]:
        request.session["result"] = 1
    if request.POST["user_number"] == request.session["random"]:
        request.session["result"] = 2
    return render(request,"index.html",context)