from django import forms
from .models import Todo

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text':forms.TextInput(attrs={'class':'form-control mb-2'}),
        }