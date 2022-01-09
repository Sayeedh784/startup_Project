from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name="home"),
    path('register/',views.register, name='register'),
    path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('startup_register/',views.startup_register.as_view(), name='startup_register'),
    path('investor_register/',views.investor_register.as_view(), name='investor_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
