from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
    }