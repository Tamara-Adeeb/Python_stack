from django.shortcuts import redirect, render
import random

def random(request):
    if "random" not in request.session:
        request.session["random"] = random.randint(1, 100)

    return render(request,"index.html")
    
def check(request):
    if "result" not in request.session:
        request.session["result"] = 0
    if int(request.POST["user_number"]) > request.session["random"]:
        request.session["result"] = 0
    if int(request.POST["user_number"]) == request.session["random"]:
        request.session["result"] = 1
    if int(request.POST["user_number"]) < request.session["random"]:
        request.session["result"] = 2
    return redirect("/")

def try_again(request):
    request.session.clear()
    return redirect("/")

