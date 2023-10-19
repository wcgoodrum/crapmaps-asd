from django.http import HttpResponse
from django.shortcuts import render
from .models import Bathroom

def index(request):
    return HttpResponse("Hello, world. You're at the crap_maps index.")

def map_view(request):
    bathrooms = Bathroom.objects.all()
    context = {'bathrooms': bathrooms}
    return render(request, 'map.html', context)