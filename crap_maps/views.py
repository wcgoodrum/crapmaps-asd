from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Bathroom, Review

def index(request):
    return HttpResponse("Hello, world. You're at the crap_maps index.")

def success(request):
    return render(request, 'success.html')

def map_view(request):
    bathrooms = Bathroom.objects.all()
    context = {'bathrooms': bathrooms}
    return render(request, 'map.html', context)

def review_view(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bathroom_id = request.POST.get('bathroom')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')

        bathroom = Bathroom.objects.get(pk=bathroom_id)

        review = Review(bathroom=bathroom, rating=rating, comment=review_text)
        print(review)
        review.save()

        return HttpResponseRedirect('success')

    bathrooms = Bathroom.objects.all()
    context = {'bathrooms': bathrooms}
    return render(request, 'review.html', context)