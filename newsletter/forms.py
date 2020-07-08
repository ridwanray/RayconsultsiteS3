from django import forms
from .models import Newsletteruser
class Newslettersignupform(forms.ModelForm):
    class Meta:
        model= Newsletteruser
        fields= ['email']

        def cleaned_email(self):
            email = self.cleaned_data.get('email')
            return email
