from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request, 'accounts/home.html')

def map(request):

    return render(request, 'accounts/map.html')