from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from multiselectfield import MultiSelectField

class User(AbstractUser):
  is_customer = models.BooleanField(default=False)
  is_investor = models.BooleanField(default=False)
  is_startup = models.BooleanField(default=False)
  friends = models.ManyToManyField('User',blank=True)

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
    ('Agritech', 'Agritech'),
    ('Robotics', 'Robotics'),
    ('Data Analysis', 'Data Analysis'),
    ('Biotech', 'Biotech'),
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
MODEL_CHOICES = (
    ('B2B', 'B2B'),
    ('B2C', 'B2C'),
    ('C2B', 'C2B'),
    ('C2C', 'C2C'),
)
class Investorinfo(models.Model):
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
  facebook_link = models.URLField(blank=True)
  linkedin_link = models.URLField(blank=True)
  twitter_link = models.URLField(blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  person1 = models.CharField(max_length=100, choices=ROLE, blank=True, null=True)
  person1_name = models.CharField(max_length=50, blank=True, null=True)
  person1_image = models.ImageField(upload_to='images/', null=True, blank=True)
  person2 = models.CharField(max_length=100, choices=ROLE, blank=True, null=True)
  person2_name = models.CharField(max_length=50, blank=True, null=True)
  person2_image = models.ImageField(
      upload_to='images/', null=True, blank=True)
  def __str__(self):
    return str(self.id)
  
  def get_absolute_url(self):
    return reverse('investor-profile', args=[str(self.id)])



class StartupInfo(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  name = models.CharField(max_length=100, null=True, blank=True)
  company_name = models.CharField(max_length=100, null=True, blank=True)
  title = models.CharField(max_length=100,blank=True,null=True)
  email = models.EmailField(max_length=100, null=True, blank=True)
  mobile = models.CharField(max_length=50, null=True, blank=True)
  logo = models.ImageField(upload_to='images/', null=True,blank=True)
  establish_year = models.IntegerField(blank=True, null=True)
  business_model = models.CharField(max_length=100, choices=MODEL_CHOICES, blank=True,null=True)
  employee_range = models.CharField(max_length=100, blank=True, null=True)
  market_presence = models.CharField(max_length=100, choices=CITY_CHOICES, blank=True, null=True)
  looking_at = models.CharField(choices=LOOK_CHOICES,max_length=100, blank=True, null=True)
  sector = models.CharField(max_length=100,choices= SECTOR, blank=True, null=True)
  description = models.TextField(max_length=1000, blank=True, null=True)
  videofile = models.FileField(upload_to='videos/', default="Not availabe",null=True, blank=True)
  weblink = models.URLField( blank=True)
  facebook_link = models.URLField(blank=True)
  linkedin_link = models.URLField(blank=True)
  twitter_link = models.URLField(blank=True)
  location = models.CharField(max_length=100, null=True, blank=True)
  person1= models.CharField(max_length=100,choices=ROLE,blank=True,null=True)
  person1_name = models.CharField(max_length=50, blank=True, null=True)
  person1_image = models.ImageField(upload_to='images/', null=True, blank=True)
  person2 = models.CharField(max_length=100, choices=ROLE, blank=True, null=True)
  person2_name = models.CharField(max_length=50, blank=True, null=True)
  person2_image = models.ImageField(upload_to='images/', null=True, blank=True)

  def __str__(self):
    return str(self.id)

  def get_absolute_url(self):
    return reverse('startup-profile', args=[str(self.id)])



class CustomerInfo(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  biography=models.TextField(max_length=500,blank=True,null=True)
  email = models.EmailField(max_length=100, blank=True, null=True)
  mobile = models.CharField(max_length=20,blank=True,null=True)
  profession = models.CharField(max_length=50,blank=True,null=True)
  looking_at = models.CharField(choices=LOOK_CHOICES, max_length=100, null=True, blank=True)
  sector = models.CharField(max_length=100, choices=SECTOR,blank=True, null=True)
  image = models.ImageField(upload_to='images/',null=True,blank=True)
  facebook_link = models.URLField(blank=True)
  linkedin_link = models.URLField(blank=True)
  twitter_link = models.URLField(blank=True)
  def __str__(self):
    return str(self.id)

  def get_absolute_url(self):
    return reverse('customer_profile', args=[str(self.id)])
  
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


class Notification(models.Model):
  notification_type = models.IntegerField()
  to_user = models.ForeignKey(User,related_name='notification_to',on_delete=models.CASCADE,null=True)
  from_user = models.ForeignKey(User,related_name='notification_from',on_delete=models.CASCADE,null=True)
  thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
  date = models.DateTimeField(auto_now_add=True)
  user_has_seen = models.BooleanField(default=False)


class ThreadModel(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')

class MessageModel(models.Model):
  thread = models.ForeignKey(ThreadModel,related_name='+',
  on_delete=models.CASCADE,blank=True,null=True)
  sender_user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  receiver_user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
  body = models.CharField(max_length=1000)
  image = models.ImageField(upload_to='message_images/',blank=True,null=True)
  date = models.DateTimeField(auto_now_add=True)
  is_read= models.BooleanField(default=False)
