from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def test(request):
    return HttpResponse("<h1 style='text-align:center;'>My First Test</h1>")
