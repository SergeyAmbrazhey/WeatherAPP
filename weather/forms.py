from .models import City
from django.forms import ModelForm, TextInput, widgets


class CitiForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'id': 'city',
                'pleceholder': 'Введите город'
            })}
