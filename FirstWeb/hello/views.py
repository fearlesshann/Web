from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def fearless(request):
    return HttpResponse(f"What's inside a Http request: \n{request}")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })