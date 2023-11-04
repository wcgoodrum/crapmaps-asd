from django import forms
from .models import Bathroom, Review

class ReviewForm(forms.Form):
    bathroom = forms.ModelChoiceField(
        queryset=Bathroom.objects.all(), 
        empty_label=None, 
        widget=forms.Select(attrs={'class': 'form-control'}))

    rating = forms.IntegerField(min_value=1, max_value=5, 
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    Review = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    
    approved_status = forms.BooleanField(default=False)
    
