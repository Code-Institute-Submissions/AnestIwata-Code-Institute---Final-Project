from django import forms
from .models import Feature


class CreateFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'description', 'project']
