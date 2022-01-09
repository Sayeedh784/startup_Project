from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  is_customer = models.BooleanField(default=False)
  is_investor = models.BooleanField(default=False)
  is_startup = models.BooleanField(default=False)
  
class Investorinfo(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True)
  establish_year = models.IntegerField(blank=True, null=True)
  investor_type = models.CharField(max_length=10, blank=True, null=True)
  employee_range = models.CharField(max_length=10, blank=True, null=True)
  market_presence = models.CharField(max_length=100, blank=True, null=True)
  looking_at = models.CharField(max_length=100, blank=True, null=True)
  tags = models.CharField(max_length=100, blank=True, null=True)
  description = models.CharField(max_length=1000, blank=True, null=True)
  videos = models.FileField(upload_to='videos/', null=True)
  weblink = models.URLField(unique=True,blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  team_member1 = models.ImageField(upload_to='images/', null=True)
  team_member2 = models.ImageField(upload_to='images/', null=True)

  def __str__(self):
    return str(self.id)


class StartupInfo(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True)
  establish_year = models.IntegerField(blank=True, null=True)
  business_model = models.CharField(max_length=100, blank=True, null=True)
  employee_range = models.CharField(max_length=100, blank=True, null=True)
  market_presence = models.CharField(max_length=100, blank=True, null=True)
  looking_at = models.CharField(max_length=100, blank=True, null=True)
  sector = models.CharField(max_length=100, blank=True, null=True)
  description = models.CharField(max_length=1000, blank=True, null=True)
  videofile = models.FileField(upload_to='videos/', null=True)
  weblink = models.URLField(unique=True, blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  team_member1 = models.ImageField(upload_to='images/', null=True)
  team_member2 = models.ImageField(upload_to='images/', null=True)

  def __str__(self):
    return str(self.id)


class CustomerInfo(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, blank=True, null=True)
  mobile = models.CharField(max_length=20,blank=True,null=True)

  def __str__(self):
    return str(self.id)
  
  




