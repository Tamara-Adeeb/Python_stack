from django.shortcuts import render,redirect
import random

def gold(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    context = {
        "total_gold": request.session["gold"]
    }
    return render(request,"index.html",context)

def total_gold(request):
    if "place" not in request.session:
        request.session["place"] == ""
    request.session["place"] = request.POST["place"]
    if "gold" not in request.session:
        request.session["gold"] = 0
    if request.session["place"] == "farm":
        request.session["gold"] += random.randint(10, 20)
    if request.session["place"] == "cave":
        request.session["gold"] += random.randint(5, 10)
    if request.session["place"] == "house":
        request.session["gold"] += random.randint(2, 5)
    if request.session["place"] == "casino":
        request.session["gold"] += random.randint(-50, 50)
    return redirect("/")
