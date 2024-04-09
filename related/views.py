from django.shortcuts import render

# Create your views here.
def related(request):
    return render(request, 'related/related.html')
