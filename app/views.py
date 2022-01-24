from django.db.models.query import EmptyQuerySet
from django.http import QueryDict, request
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView,ListView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from app.models import *
from .filters import *


def home(request):
  startup = StartupInfo.objects.all()
  total_startup = startup.count()
  investor = Investorinfo.objects.all()
  total_investor = investor.count()
  customer = CustomerInfo.objects.all()
  total_customer = customer.count()
  context = {'total_startup': total_startup,
             'total_investor': total_investor, 'total_customer': total_customer, }
  return render(request,'app/home.html',context)


def register(request):
    return render(request, 'app/register.html')


class customer_register(View):
  def get(self, request):
    form = CustomersignUpForm()
    return render(request, 'app/customer_register.html', {'form': form})

  def post(self, request):
    form = CustomersignUpForm(request.POST)
    if form.is_valid():
      messages.success(request, "Congratulations!!! Registered successfully")
      form.save()
    return redirect('/login')
class startup_register(View):
  def get(self, request):
    form = StartupsignUpForm()
    return render(request, 'app/startup_register.html', {'form': form})

  def post(self, request):
    form = StartupsignUpForm(request.POST)
    if form.is_valid():
      messages.success(request, "Congratulations!!! Registered successfully")
      form.save()
    return redirect('/login')
class investor_register(View):
  def get(self, request):
    form = InvestorsignUpForm()
    return render(request, 'app/investor_register.html', {'form': form})

  def post(self, request):
    form = InvestorsignUpForm(request.POST)
    if form.is_valid():
      messages.success(request, "Congratulations!!! Registered successfully")
      form.save()
    # return render(request, 'app/investor_register.html', {'form': form})
    return redirect('/login')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'app/login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/login')

def userProfileForm(request,pk):
  if request.method == "POST":
    if request.user.is_startup:
      obj = get_object_or_404(StartupInfo, user_id=request.user.id)
      form = Startup_profileForm(request.POST,instance=obj)
    elif request.user.is_investor:
      obj = get_object_or_404(Investorinfo, user_id=request.user.id)
      print()
      form = Investor_profileForm(request.POST, instance=obj)
    elif request.user.is_customer:
      obj = get_object_or_404(CustomerInfo, user_id=request.user.id)
      form = Customer_profileForm(request.POST, instance=obj)
    if form.is_valid():
      form.save()
      if request.user.is_startup:
        form = Startup_profileForm()
      elif request.user.is_investor:
        form = Investor_profileForm()
      else:
        form = Customer_profileForm()
      messages.success(request,"Profile Updated successfully!!!")
  else:
    if request.user.is_startup:
      form = Startup_profileForm()
    elif request.user.is_investor:
      form = Investor_profileForm()
    elif request.user.is_customer:
      form = Customer_profileForm()
  context={'form':form}
  
  return render(request,'app/user_profileForm.html',context)
  
def profile(request,pk):
  
  if request.user.is_startup:
    startup = StartupInfo.objects.get(user_id=request.user.id)
    return render(request, 'app/startup_profile.html', {'startup': startup})
  elif request.user.is_investor:
    investor = Investorinfo.objects.get(user_id=request.user.id)
    return render(request, 'app/investor_profile.html', {'investor': investor})
  elif request.user.is_customer:
    customer = CustomerInfo.objects.get(user_id=request.user.id)
    return render(request, 'app/customer_profile.html', {'customer': customer})

def startup_profile(request,pk):
  startup = StartupInfo.objects.get(pk=pk)
  return render(request, 'app/startup_profile.html', {'startup': startup})

def startup_home(request):
  startups = StartupInfo.objects.all()
  
  myfilter = StartupFilter(request.GET,queryset=startups)
  startups = myfilter.qs
  after_filter = startups.count()
  context = {'startups': startups,'myfilter': myfilter, 'after_filter': after_filter}
  return render(request, 'app/startup_home.html',context)

def investor_profile(request,pk):
  investor = Investorinfo.objects.get(pk=pk)
  return render(request, 'app/investor_profile.html', {'investor': investor})

def investor_home(request):
  investors = Investorinfo.objects.all()
  myfilter = InvestorFilter(request.GET, queryset=investors)
  investors = myfilter.qs
  after_filter = investors.count()
  context = {'investors': investors, 'myfilter': myfilter,'after_filter':after_filter}
  return render(request, 'app/investor_home.html',context)




def customer(request):
  return render(request, 'app/customer_home.html')

def article(request):
  return render(request, 'app/article.html')