from django.db.models import fields
from django.forms import widgets
import django_filters
from .models import *
from django import forms

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ['bloodgroup','location']
        label = {}
        widgets = {
            'bloodgroup': forms.Select(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }