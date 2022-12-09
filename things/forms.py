from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):
    name = forms.CharField(label='name', max_length=35)
    description = forms.CharField(label='description',max_length=120, widget=forms.Textarea)
    quantity = forms.IntegerField(label='quantity' , validators=[MinValueValidator(0),MaxValueValidator(50)],  widget=forms.NumberInput)