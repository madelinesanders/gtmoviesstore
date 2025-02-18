from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']