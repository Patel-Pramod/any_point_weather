from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    return render(request,"index.html")
def weather(request):
    return render(request,"weather.html")