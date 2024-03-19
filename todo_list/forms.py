from django import forms
from .models import TodoModel
class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        exclude = ['user','is_complete']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }