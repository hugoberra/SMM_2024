from django import forms
from .models import Municipality

class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = ['name', 'city', 'rfc', 'government', 'status']