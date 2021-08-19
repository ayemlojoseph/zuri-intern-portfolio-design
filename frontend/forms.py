from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget




class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
       'placeholder': 'Enter Email',
       'class': 'form-control'
    }))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
       'placeholder': 'Write message',
       'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-15'
    }))