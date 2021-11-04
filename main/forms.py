from django import forms
from .models import Reviews,Rating,RatingStart


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['email', 'name', 'text']


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStart.objects.all(), widget=forms.RadioSelect(),empty_label=None
    )
    class Meta:
        model = Rating
        fields = ('star',)