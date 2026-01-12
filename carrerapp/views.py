from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "carrerapp/index.html")

def history(request):
    return render(request, "carrerapp/history.html")
