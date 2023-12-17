

from django import forms
from .models import ImageModel

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'description', 'image','video']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
