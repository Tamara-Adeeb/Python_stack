from dojo_ninjas_app.models import Dojos
from django.shortcuts import redirect, render
from . import models
from dojo_ninjas_app.models import Ninjas,Dojos

def home(request):
    context = {
        "Dojo" : Dojos.objects.all(),
        "Ninja" : Ninjas.objects.all()
    }
    return render(request,"index.html",context)

def add(request):
    if request.POST["add_data"] == "Dojo":
        Dojos.objects.create(name=request.POST["name"], city=request.POST["city"],state=request.POST["state"])
        # list = []
        # x = Dojos.objects.create(name=request.POST["name"], city=request.POST["city"],state=request.POST["state"])
        # list.append(x)
        # print(x)
        # request.session["dojo"] = list  
        return redirect("/")
    if request.POST["add_data"] == "Ninja":
        Ninjas.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"], dojo_id=Dojos.objects.get(id = int(request.POST["dojo"])))
        return redirect("/")
