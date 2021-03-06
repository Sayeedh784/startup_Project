from django.forms import fields, forms
import django_filters
from .models import *


class StartupFilter(django_filters.FilterSet):
  class Meta:
    model = StartupInfo
    fields = ('sector','market_presence','looking_at','business_model')
    

class InvestorFilter(django_filters.FilterSet):
  class Meta:
    model = Investorinfo
    fields = ('tags','market_presence','looking_at','investor_type')

class CustomerFilter(django_filters.FilterSet):
  class Meta:
    model = CustomerInfo
    fields=('sector','profession','looking_at')