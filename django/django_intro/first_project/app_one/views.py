from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def test(request):
    return HttpResponse("<h1 style='text-align:center;'>My First Test</h1>")

def name(request, name, color):
    context = {
        "user_name" : name,
        "my_color" : color
    }
    # color = color Hoe i can pass color alone
    return render(request, "index.html", context)