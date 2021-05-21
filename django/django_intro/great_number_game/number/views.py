from django.shortcuts import redirect, render
import random

def random(request):
    if "random" not in request.session:
        request.session["random"] = random.randint(1, 100)
    context = {
        "random": request.session["random"],
        "number": request.session["number"],
        "result": request.session["result"]
    }
    return render(request,"index.html",context)
    
def check(request):
    if "result" not in request.session:
        request.session["result"] = 0
    request.session["number"] = int(request.POST["user_number"])
    if request.session["number"] > request.session["random"]:
        request.session["result"] = 0
    if request.session["number"] == request.session["random"]:
        request.session["result"] = 1
    if request.session["number"] < request.session["random"]:
        request.session["result"] = 2
    
    return redirect("/")

