from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from app.models import *



def home(request):
  return render(request,'app/home.html')


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

# class customer_register(CreateView):
#     model = User
    
#     form_class = CustomersignUpForm
#     template_name = 'app/customer_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')

# class investor_register(CreateView):
#     model = User
#     form_class = InvestorsignUpForm
#     template_name = 'app/employee_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')
# class startup_register(CreateView):
#     model = User
#     form_class = StartupsignUpForm
#     template_name = 'app/employee_register.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/login')


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
    return render(request, 'app/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/login')

