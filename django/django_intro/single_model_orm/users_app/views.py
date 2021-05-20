from django.shortcuts import redirect, render
from .models import Users

def home(request):

    context = {
        "x": Users.objects.all()
    }
    return render(request,"index.html",context)

def data(request):
    Users.objects.create(first_name=request.POST["first_name"], last_name = request.POST["last_name"],email_address=request.POST["email"],age=int(request.POST["age"]))
    return redirect("/")