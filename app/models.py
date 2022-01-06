
from django.db import models


class Investorinfo(models.Model):
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True)
  establish_year = models.IntegerField(blank=True, null=True)
  investor_type = models.CharField(max_length=10, blank=True, null=True)
  employee_range = models.CharField(max_length=10, blank=True, null=True)
  market_presence = models.CharField(max_length=100, blank=True, null=True)
  lokking_at = models.CharField(max_length=100, blank=True, null=True)
  tags = models.CharField(max_length=100, blank=True, null=True)
  description = models.CharField(max_length=1000, blank=True, null=True)
  videos = models.FileField(upload_to='videos/', null=True)
  weblink = models.URLField(unique=True,blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  team_member1 = models.ImageField(upload_to='images/', null=True)
  team_member2 = models.ImageField(upload_to='images/', null=True)

  def __str__(self):
    return self.company_name


class StartupInfo(models.Model):
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True)
  establish_year = models.IntegerField(blank=True, null=True)
  business_model = models.CharField(max_length=100, blank=True, null=True)
  employee_range = models.CharField(max_length=100, blank=True, null=True)
  market_presence = models.CharField(max_length=100, blank=True, null=True)
  lokking_at = models.CharField(max_length=100, blank=True, null=True)
  sector = models.CharField(max_length=100, blank=True, null=True)
  description = models.CharField(max_length=1000, blank=True, null=True)
  videofile = models.FileField(upload_to='videos/', null=True)
  weblink = models.URLField(unique=True, blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  team_member1 = models.ImageField(upload_to='images/', null=True)
  team_member2 = models.ImageField(upload_to='images/', null=True)

  def __Str__(self):
    return self.company_name


class CustomerInfo(models.Model):
  name = models.CharField(max_length=100, null=True, blank=True)
  email = models.EmailField(max_length=100, blank=True, null=True)
  mobile = models.CharField(max_length=20,blank=True,null=True)

  def __str__(self):
    return self.name
  
  




