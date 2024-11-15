from wsgiref.validate import validator

from django import forms
from .models import Contacts
from django.core.validators import MinLengthValidator
class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name','email','phone','message']

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message) < 100:
            raise forms.ValidationError("Message must be at least 100 characters long.")
        return message