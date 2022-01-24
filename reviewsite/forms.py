from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """ Game Review Form """

    class Meta:
        model = Review
        fields = ('score', 'body')
