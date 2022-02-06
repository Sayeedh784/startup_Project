from django.contrib import admin
from .models import *


admin.site.register(User)
@admin.register(StartupInfo)
class StartupModelAdmin(admin.ModelAdmin):
  list_display = ['id','user','name','company_name','email']
@admin.register(Investorinfo)
class InvestorAdminModel(admin.ModelAdmin):
  list_display = ['id', 'user', 'name', 'company_name', 'email']
@admin.register(CustomerInfo)
class CustomerAdminModel(admin.ModelAdmin):
  list_display = ['id','user','name','email','sector']
  
@admin.register(ReviewRating)
class RewviewRating(admin.ModelAdmin):
  list_display=['id','rating','created_at']
@admin.register(InvestorReviewRating)
class InvestorRewviewRating(admin.ModelAdmin):
  list_display=['id','rating','created_at']
