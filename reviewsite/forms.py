from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    score = forms.DecimalField(decimal_places=2, max_digits=3, min_value=0, max_value=5)

    class Meta:
        model = Review
        fields = ('score', 'body')
        