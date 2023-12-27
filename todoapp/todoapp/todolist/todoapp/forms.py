from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control text-center'}),
            'details': forms.Textarea(attrs={'class': 'form-control text-center', 'style': 'height: 150px;'}),
            'date': forms.TextInput(attrs={'class': 'form-control text-center'}),
        }
