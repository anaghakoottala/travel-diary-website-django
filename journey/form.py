from django import forms
from django.forms import ModelForm,TextInput
from .models import Memory

class MemForm(forms.Form):
    image = forms.ImageField()
    class Meta:
        model=Memory
        exclude = ['title','place','desc']
        #fields=['image']
        #widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}
