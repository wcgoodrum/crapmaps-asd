from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import map_view, review_view, success

from . import views

app_name="crap_maps"
urlpatterns = [
    # path("", views.index, name="index"),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('map/', map_view, name='map'),
    path('review/', review_view, name='review'), 
    path('review/success/', TemplateView.as_view(template_name="success.html"))
]
