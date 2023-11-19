from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Bathroom, Review
from django.contrib.auth.decorators import user_passes_test, login_required

def index(request):
    return HttpResponse("Hello, world. You're at the crap_maps index.")

def success(request):
    return render(request, 'success.html')

@login_required
def map_view(request):
    bathrooms = Bathroom.objects.all()
    reviews = Review.objects.filter(approved_status=True)
    context = {'bathrooms': bathrooms, 'reviews' : reviews}
    return render(request, 'map.html', context)

@login_required
def review_view(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        bathroom_id = request.POST.get('bathroom')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')

        bathroom = Bathroom.objects.get(pk=bathroom_id)

        review = Review(bathroom=bathroom, rating=rating, comment=review_text)
        review.save()

        return HttpResponseRedirect('success')

    bathrooms = Bathroom.objects.all()
    context = {'bathrooms': bathrooms, 'is_admin': request.user.groups.filter(name='admin').exists()}
    return render(request, 'review.html', context)

@login_required
def approve_view(request):

    if not request.user.groups.filter(name='admin').exists():
        return render(request, 'not_admin.html')

    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        action = request.POST.get('action')

        print(review_id)
        print(action)

        if action == 'approve':
            review = Review.objects.get(pk=review_id)
            review.approved_status = True
            review.save()
        elif action == 'deny':
            review = Review.objects.get(pk=review_id)
            review.delete()

    unapproved_reviews = Review.objects.filter(approved_status=0)
    context = {'unapproved_reviews': unapproved_reviews}
    return render(request, 'approve.html', context)
