from django.shortcuts import render,redirect
import random

def gold(request):
    # if "gold" not in request.session:
    #     request.session["gold"] = 0
    return render(request,"index.html")

def total_gold(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "active" not in request.session:
        request.session["active"] = []
    place = request.POST["place"]
    if request.POST["place"] == "farm":
        x = random.randint(10, 20)
        request.session["gold"] += x
    if request.POST["place"] == "cave":
        x = random.randint(5, 10)
        request.session["gold"] += x
    if request.POST["place"] == "house":
        x = random.randint(2, 5)
        request.session["gold"] += x
    if request.POST["place"] == "casino":
        x = random.randint(-50, 50)
        request.session["gold"] += x
    if x >= 0:
        request.session["active"].append(f"Earned {x} golds from the {place}!")
    if x < 0 :
        request.session["active"].append(f"Entered a casino and lost {x} golds...Ouch")

    return redirect("/")