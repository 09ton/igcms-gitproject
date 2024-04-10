from django.shortcuts import render

# Create your views here.
def incidents(request):
    return render(request, 'incidents/incidents.html')
