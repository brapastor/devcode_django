from django import forms
from .models import User

class ExtraDataForms(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')