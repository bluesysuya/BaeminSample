from django.forms import ModelForm
from .models import Partner
from django import forms

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "name",
            "contact",
            "address",
            "description",
        )
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "contact": forms.TextInput(attrs={"class":"form-control"}),
            "address": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
        }
