from django.http import QueryDict, request
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template import context
from django.views import View
from django.views.generic import CreateView,ListView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from app.models import *
from .filters import *
from .import form
from django.core.paginator import Paginator


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
      form = Investor_profileForm(request.POST, instance=obj)
    elif request.user.is_customer:
      obj = get_object_or_404(CustomerInfo, user_id=request.user.id)
      form = Customer_profileForm(request.POST, instance=obj)
    if form.is_valid():
      form.save()
      if request.user.is_startup:
        startup = StartupInfo.objects.get(user_id=request.user.id)
        return render(request, 'app/startup_profile.html', {'startup': startup})
      elif request.user.is_investor:
        investor = Investorinfo.objects.get(user_id=request.user.id)
        return render(request, 'app/investor_profile.html', {'investor': investor})
      elif request.user.is_customer:
        customer = CustomerInfo.objects.get(user_id=request.user.id)
        return render(request, 'app/customer_profile.html', {'customer': customer})
        # messages.success(request, "Profile Updated successfully!!!")
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
  reviews = ReviewRating.objects.filter(startup_id=startup.id, status=True)
  count = reviews.count()
  
  return render(request, 'app/startup_profile.html', {'startup': startup,'reviews':reviews,'count':count})

def startup_home(request):
  startups = StartupInfo.objects.all()
  myfilter = StartupFilter(request.GET,queryset=startups)
  startups = myfilter.qs
  after_filter = startups.count()
  page = Paginator(startups, per_page=1)
  page_list = request.GET.get('page')
  page = page.get_page(page_list)
  context = {'startups': startups,'page':page,'myfilter': myfilter, 'after_filter': after_filter}
  return render(request, 'app/startup_home.html',context)

def investor_profile(request,pk):
  investor = Investorinfo.objects.get(pk=pk)
  reviews = InvestorReviewRating.objects.filter(investor_id=investor.id, status=True)
  count = reviews.count()
  return render(request, 'app/investor_profile.html', {'investor': investor,'reviews':reviews,'count':count})

def investor_home(request):
  investors = Investorinfo.objects.all()
  myfilter = InvestorFilter(request.GET, queryset=investors)
  investors = myfilter.qs
  after_filter = investors.count()
  page = Paginator(investors, per_page=1)
  page_list = request.GET.get('page')
  page = page.get_page(page_list)
  context = {'investors': investors, 'page':page,'myfilter': myfilter,'after_filter':after_filter}
  return render(request, 'app/investor_home.html',context)




def customer(request):
  return render(request, 'app/customer_home.html')

def article(request):
  return render(request, 'app/article.html')



def submit_review(request,startup_id):
  url=request.META.get('HTTP_REFERER')
  if request.method == 'POST':
    try:
      reviews=ReviewRating.objects.get(user_id=request.user.id, startup_id=startup_id)
      form=ReviewForm(request.POST, instance=reviews)
      form.save()
      messages.success(
          request, 'Thank you! Your review has been updated.')
      return redirect(url)
    except ReviewRating.DoesNotExist:
      form=ReviewForm(request.POST)
      if form.is_valid():
          data=ReviewRating()
          data.rating=form.cleaned_data['rating']
          data.review=form.cleaned_data['review']
          data.startup_id=startup_id
          data.user_id=request.user.id
          data.save()
          
          return redirect(url)

def investor_submit_review(request,investor_id):
  url=request.META.get('HTTP_REFERER')
  if request.method == 'POST':
    try:
      reviews=InvestorReviewRating.objects.get(user_id=request.user.id, investor_id=investor_id)
      form=Investor_ReviewForm(request.POST, instance=reviews)
      form.save()
      messages.success(
          request, 'Thank you! Your review has been updated.')
      return redirect(url)
    except InvestorReviewRating.DoesNotExist:
      form=Investor_ReviewForm(request.POST)
      if form.is_valid():
          data=InvestorReviewRating()
          data.rating=form.cleaned_data['rating']
          data.review=form.cleaned_data['review']
          data.investor_id=investor_id
          data.user_id=request.user.id
          data.save()
          
          return redirect(url)


def paginator(request):
  startups=StartupInfo.objects.all()
  page= Paginator(startups,per_page=1)
  page_number=request.GET.get('page',1)
  page_obj=page.get_page(page_number)
  context={'startups':page_obj.object_list,'page':page}
  return render(request,'startup_home.html',context)
