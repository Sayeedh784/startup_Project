from django.forms import fields, forms
import django_filters
from .models import *
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _

class StartupFilter(django_filters.FilterSet):
  class Meta:
    model = StartupInfo
    fields = ('sector','market_presence','looking_at','business_model')
    

class InvestorFilter(django_filters.FilterSet):
  class Meta:
    model = Investorinfo
    fields = ('tags','market_presence','looking_at','investor_type')
