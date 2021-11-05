from django import forms
from .models import Reviews,Rating,RatingStart
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Reviews
        fields = ['email', 'name', 'text', 'captcha']
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control border'}),
            'email': forms.EmailInput(attrs={'class':'form-control border'}),
            'text': forms.Textarea(attrs={'class':'form-control border'})
        }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStart.objects.all(), widget=forms.RadioSelect(),empty_label=None
    )
    class Meta:
        model = Rating
        fields = ('star',)