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

@admin.register(ThreadModel)
class ThreadModelAdmin(admin.ModelAdmin):
  list_display=['id','user','receiver']

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
  list_display=['id','sender_user','receiver_user','date']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
  list_display=['id','from_user','to_user','date']