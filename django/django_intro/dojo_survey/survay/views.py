from django.shortcuts import render

def login_form(request):
    # location = ["Palestine", "China", "Japan"]
    # gender = ["Female", "Male"]
    # language = ["Python","Marne","Java","JavaScript"]
    context = {
        "location" : ["Palestine", "China", "Japan"],
        "gender" : ["Female", "Male"],
        "language" : ["Python","Marne","Java","JavaScript"]
    }
    return render(request,"index.html",context)

def show(request):
    if request.method == "POST":
        list = []
        for i in request.POST:
            list.append(request.POST[i])
        context = {
            "list" : list
        }
        return render(request,"user_info.html",context)
