from django import forms
from django.core import validators
from django.db.models import fields

from django.forms.widgets import Widget
from myapp import models
from datetime import date, datetime

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):


    phone = forms.IntegerField(
        required=False,
        widget =forms.TextInput(
            attrs={
                'class':'form-control', 'placeholder':'Phone Number','pattern':'[0-9]*','title':'Contain only digits!'
                }
            )
        )

    class Meta:
        model = models.Donor
        fields = ['name' ,'email', 'location' , 'phone'  , 'lastdonationdate', 'bloodgroup']

        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Name','pattern':'[A-Za-z|\s]+','title':'Name should contain only characters!'}),

            'email': forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'johndone@email.com'}),
            
            'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location','pattern':'[^0-9]+','title':'only district name'}),

            
            'lastdonationdate': forms.DateInput(attrs={'type':'date' , 'title':'No future date is '}),
            
            'bloodgroup': forms.Select(attrs={'class':'form-group' , 'placeholder':'Blood Group'})
        }
    def clean_phone(self):
        cleaned_data = super().clean()
        phone = self.cleaned_data.get('phone')
        if phone<8:
            raise forms.ValidationError("No futre date")     
        else:
            return phone


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']