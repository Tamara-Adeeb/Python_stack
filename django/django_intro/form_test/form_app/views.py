from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def info(request):
    print(request.POST) #output:<QueryDict: 
    #{'csrfmiddlewaretoken': ['ieXl6P0Z2tTnX3s4ZUZ2iPCrPLgVMYyCev4oIDe6Py617SkqDuzxM8VM0wgZPmhc'], 
    # 'name': ['Tamaraafs'], 'email': ['dgdfg']}>
    # if request.method == "POST":
    context = {
        "user_name" : request.POST["name"],
        "user_email" : request.POST["email"]
    }
    print(context)#output:{'user_name': 'Tamaraafs', 'user_email': 'dgdfg'}

    return render(request, "info.html",context)
