from django import forms
from .models import Role

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']

    # Add placeholders directly in the form fields
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Role Name to be created',
        'class': 'form-control'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Add Role Description',
        'class': 'form-control'
    }))
