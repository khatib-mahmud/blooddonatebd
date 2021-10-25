from datetime import date, datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator



phone_regex = RegexValidator(r'^[0-9]*$',"no characters")

name_regex = RegexValidator(r'^[a-zA-Z|\s]+$',"no numeric")

class Donor(models.Model):
    
    group = [
       ('A+','A+'),
       ('A-' , 'A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('Ab+','Ab+'),
        ('Ab-','Ab-'),
        ('O+','O+'),
        ('O-','O-'),
    ]
    name = models.CharField( max_length=50, validators=[name_regex])
    email = models.EmailField( max_length=254)
    location = models.CharField(max_length=50,blank=False)
    phone = models.CharField(blank=False, max_length=11)
        
    lastdonationdate = models.DateField(auto_now=False, auto_now_add=False)
      
    bloodgroup = models.CharField( max_length=4 ,choices=group)

    

    def __str__(self):
        return self.name + " "+ self.bloodgroup
    
    
        