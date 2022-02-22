from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *
from django.forms import fields, widgets
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm, AuthenticationForm, UsernameField
PasswordChangeForm, PasswordResetForm, SetPasswordForm


class StartupsignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
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
    email = forms.EmailField(max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
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
    

class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label=_("Old Password"),
  strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,
 'class': 'form-control'}))
  new_password1 = forms.CharField(label=_("New Password"),
  strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'New password',
  'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
  new_password2 = forms.CharField(label=_("Confrim New Password"),
  strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
  'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
  email  = forms.EmailField(label=_("Email"),max_length=254,
  widget=forms.EmailInput(attrs={'autocomplete':'email',
  'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
  new_password1= forms.CharField(label=_("New Password"),
  strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
  'class':'form-control'}),help_text=password_validation.
  password_validators_help_text_html())
  new_password2= forms.CharField(label=_("Comfrim New Password"),
  strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',
  'class':'form-control'}))


class Startup_profileForm(forms.ModelForm):
    class Meta:
        model = StartupInfo
        fields = ['name', 'company_name','title','email','mobile','logo','establish_year','business_model','employee_range',
                  'market_presence', 'looking_at', 'sector', 'description', 'videofile', 'weblink', 'facebook_link', 'linkedin_link', 'twitter_link', 'location',
                  'person1', 'person1_name', 'person1_image', 'person2', 'person2_name', 'person2_image']
        

class Investor_profileForm(forms.ModelForm):
    class Meta:
        model = Investorinfo
        fields = ['name', 'company_name','title', 'email', 'mobile', 'logo', 'establish_year', 'investor_type', 'employee_range',
        'market_presence', 'looking_at', 'tags', 'description', 'videos', 'weblink','facebook_link','linkedin_link','twitter_link', 'location',
        'person1','person1_name','person1_image','person2','person2_name','person2_image']
class Customer_profileForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['name', 'mobile', 'email', 'profession', 'biography', 'looking_at','sector', 'image','facebook_link', 'linkedin_link', 'twitter_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = [ 'review', 'rating']
class Investor_ReviewForm(forms.ModelForm):
    class Meta:
        model = InvestorReviewRating
        fields = [ 'review', 'rating']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)
