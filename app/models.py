from contextlib import nullcontext
from email.policy import default
from statistics import mode
from turtle import title
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField

class User(AbstractUser):
  is_customer = models.BooleanField(default=False)
  is_investor = models.BooleanField(default=False)
  is_startup = models.BooleanField(default=False)

CITY_CHOICES = (
  ('Dhaka','Dhaka'),
  ('Khulna',"khulna"),
  ('Barishal','Barishal'),
  ('Rajsahi','Rajsahi'),
  ('Chittagong','Chittagong'),
  ('Shylet','Shylet'),
  ('Rangpur','Rangpur'),
  ('Mymensing','Mymensing'),
)
SECTOR = (
    ('AI', 'AI'),
    ('Robotics', 'Robotics'),
    ('Data Analysis', 'Data Analysis'),
    ('Biotech', 'Biotech'),
    ('Agritech', 'Agritech'),
    ('Bigdata', 'Bigdata'),
    ('Blockchain', 'Blockchain'),
    ('cybersecurity', 'cybersecurity'),
    ('Digital Health', 'Digital Health'),
    ('Education', 'Education'),
    ('E-commerce', 'E-commerce'),
    ('Entertainments', 'Entertainments'),
    ('Events', 'Events'),
    ('Food&Beverage', 'Food&Beverage'),
    ('Fintech', 'Fintech'),
    ('Food Science & Technology', 'Food Science & Technology'),
    ('Gaming', 'Gaming'),
    ('Hardware', 'Hardware'),
    ('Healthcare', 'Healthcare'),
    ('Infotech', 'Inftech'),
    ('IOT', 'IOT'),
    ('Manufacturing & Engineering', 'Manufacturing & Engineering'),
    ('Media', 'Media'),
    ('Nanotechnology', 'Nanotechnology'),
    ('Pharmaceutical', 'Pharmaceutical'),
    ('Real Estate', 'Real Estate'),
    ('Telecom', 'Telecom'),
    ('Trasport', 'Transport'),
    ('Travel & Hospitality', 'Travel & Hospitality'),
    ('Others', 'Others'),
)
INVSETOR_TYPE = (
  ('Angel Investor','Angel Investor'),
  ('Peer to peer Lenders','peer to peer Lenders'),
  ('Personal Investors','Personal Investors'),
  ('Bank','Bank'),
  ('Venture Capitalists', 'Venture Capitalists')
)
ROLE = (
    ('CEO', 'CEO'),
    ('Founder', 'Founder'),
    ('CEO & Founder', 'CEO & Founder'),
    ('Co-Founder', 'Co-Founder'),
    ('Manager', 'Manager'),
)
LOOK_CHOICES = (
    ('Finding Investees', 'Finding Investees'),
    ('Partnerships with Corporates', 'Partnerships with Corporates'),
    ('Partnerships with Startups', 'Partnerships with Startups'),
    ('Finding Investors', 'Finding Investors'),
    ('Finding Mentors', 'Finding Mentors'),
    ('others','others'),
)
class Investorinfo(models.Model):
  
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  title = models.CharField(max_length=100,blank=True,null = True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True, blank=True)
  establish_year = models.IntegerField(blank=True, null=True)
  investor_type = models.CharField(max_length=50,choices=INVSETOR_TYPE, blank=True, null=True)
  employee_range = models.CharField(max_length=10, blank=True, null=True)
  market_presence = models.CharField(max_length=100,choices=CITY_CHOICES, null=True, blank=True)
  looking_at = models.CharField(choices=LOOK_CHOICES, max_length=100,null=True,blank=True)
  tags = models.CharField(max_length=100,choices=SECTOR, blank=True, null=True)
  description = models.TextField(max_length=1000, blank=True, null=True)
  videos = models.FileField(upload_to='videos/', null=True,blank=True)
  weblink = models.URLField(null=True,blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  select_role1 = models.CharField(
      max_length=100, choices=ROLE, blank=True, null=True)
  selected_role_name1 = models.CharField(max_length=50, blank=True, null=True)
  selected_role_image1 = models.ImageField(
      upload_to='images/', null=True, blank=True)
  select_role2 = models.CharField(
      max_length=100, choices=ROLE, blank=True, null=True)
  selected_role_name2 = models.CharField(max_length=50, blank=True, null=True)
  selected_role_image2 = models.ImageField(
      upload_to='images/', null=True, blank=True)
  def __str__(self):
    return str(self.id)

MODEL_CHOICES=(
  ('B2B','B2B'),
  ('B2C','B2C'),
  ('C2B','C2B'),
  ('C2C','C2C'),
)





class StartupInfo(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  title = models.CharField(max_length=100,blank=True,null=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/',null=True,blank=True)
  establish_year = models.IntegerField(blank=True, null=True)
  business_model = models.CharField(max_length=100, choices=MODEL_CHOICES, blank=True,null=True)
  employee_range = models.CharField(max_length=100, blank=True, null=True)
  market_presence = models.CharField(
      max_length=100, choices=CITY_CHOICES, blank=True, null=True)
  looking_at = models.CharField(choices=LOOK_CHOICES,max_length=100, blank=True, null=True)
  sector = models.CharField(max_length=100,choices= SECTOR, blank=True, null=True)
  description = models.TextField(max_length=1000, blank=True, null=True)
  videofile = models.FileField(upload_to='videos/', default="Not availabe",null=True, blank=True)
  weblink = models.URLField( blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  select_role1= models.CharField(max_length=100,choices=ROLE,blank=True,null=True)
  selected_role_name1=models.CharField(max_length=50,blank=True,null=True)
  selected_role_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
  select_role2 = models.CharField(max_length=100, choices=ROLE, blank=True, null=True)
  selected_role_name2 = models.CharField(max_length=50, blank=True, null=True)
  selected_role_image2 = models.ImageField(upload_to='images/', null=True, blank=True)

  def __str__(self):
    return str(self.id)


class CustomerInfo(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, blank=True, null=True)
  mobile = models.CharField(max_length=20,blank=True,null=True)
  looking_at = models.CharField(choices=LOOK_CHOICES, max_length=100, null=True, blank=True)
  sector = models.CharField(max_length=100, blank=True, null=True)
  

  def __str__(self):
    return str(self.id)
  
  


class ReviewRating(models.Model):
    startup = models.ForeignKey(StartupInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return str(self.id)
class InvestorReviewRating(models.Model):
    investor = models.ForeignKey(Investorinfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return str(self.id)
