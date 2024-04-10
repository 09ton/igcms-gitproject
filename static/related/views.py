from django.shortcuts import render, get_object_or_404
from .models import Related
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def related(request):
    related = Related.objects.order_by('-held_on')
    paginator = Paginator(Related, 3)
    page = request.GET.get('page')
    paged_related = paginator.get_page(page)
    data = {
    'related' : paged_related,
    }
    return render(request, 'pages/home.html', data)

def related_detail(request, id):
    single_related = get_object_or_404(Related, pk=id)
    data = {
        'single_related': single_related,
    }
    return render(request, 'related/related_detail.html', data)
