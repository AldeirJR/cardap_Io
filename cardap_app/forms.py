from django import forms
from django.forms import ModelForm

from .models  import  *

class MyForm(forms.ModelForm):
    prompt = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:

        model = Prompt
        fields = '__all__' 
