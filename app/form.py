from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class StartupsignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=100)



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','company_name', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': "form-control"})}
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_startup = True
        user.save()

        startup = StartupInfo.objects.create(user=user)
        startup.company_name = self.cleaned_data.get('company_name')
        startup.email = self.cleaned_data.get('email')
        startup.save()
        return user


class InvestorsignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','company_name', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': "form-control"})}
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_investor = True
        
        user.save()
        investor = Investorinfo.objects.create(user=user)
        investor.company_name = self.cleaned_data.get('company_name')
        investor.email = self.cleaned_data.get('email')
        investor.save()
        return user


class CustomersignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': "form-control"})}
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        
        user.save()
        customer = CustomerInfo.objects.create(user=user)
        customer.email = self.cleaned_data.get('email')
        customer.save()
        return user
    

