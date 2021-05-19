from django.shortcuts import render,redirect

def root(request):
    if "time" not in request.session:
        request.session["time"] = 0
    if "counter" not in request.session:
            request.session["counter"] = 0
    request.session["time"] += 1
    context = {
        "time": request.session["time"],
        "counter": request.session["counter"]
    }
    return render(request,"index.html", context)

def clear(request):
    if request.method == "POST":
        request.session.clear()
    return redirect("/")

def add_2(request):
    if "counter" not in request.session:
            request.session["counter"] = 0
    if "time" not in request.session:
        request.session["time"] = 0
    else:
        request.session["time"] -= 1
    if request.method == "POST":
        
        request.session["counter"] += 2
        context = {
        "counter": request.session["counter"],
        "time": request.session["time"]
        
    }
    return redirect("/")

def add_random(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    if "time" not in request.session:
        request.session["time"] = 0
    else:
        request.session["time"] -= 1

    if request.method == "POST":
        request.session["counter"] += int(request.POST["random"])
        context = {
            "counter": request.session["counter"],
            "time": request.session["time"]
        }
    return redirect("/")