from django.shortcuts import render
from .models import Team
from related.models import Related
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    teams = Team.objects.all()
    all_relateds = Related.objects.order_by('-created_date')
    paginator = Paginator(all_relateds, 3)  
    page = request.GET.get('page')
    paged_related = paginator.get_page(page)
    data = {
        'teams': teams,
        'all_relateds': paged_related,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def transparency(request):
    return render(request, 'pages/transparency.html')

def services(request):
    return render(request, 'pages/services.html')
