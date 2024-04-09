from django.shortcuts import render
from .models import Team
from related.models import Related
# Create your views here.

def home(request):
    teams = Team.objects.all()
    all_relateds = Related.objects.order_by('-created_date')
    data = {
        'teams' : teams,
        'all_relateds' : all_relateds,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def transparency(request):
    return render(request, 'pages/transparency.html')

def services(request):
        return render(request, 'pages/services.html')
