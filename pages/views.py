from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def transparency(request):
    return render(request, 'pages/transparency.html')

def services(request):
        return render(request, 'pages/services.html')
