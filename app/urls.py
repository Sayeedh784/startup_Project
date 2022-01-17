from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .form import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name="home"),
    path('register/',views.register, name='register'),
    path('customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('startup_register/',views.startup_register.as_view(), name='startup_register'),
    path('investor_register/',views.investor_register.as_view(), name='investor_register'),
    path('user_profileForm/<str:pk>/', views.userProfileForm, name='user-form'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('startup_home/',views.startup_home,name='startup_home'),
    path('investor_home/',views.investor_home,name='investor_home'),
    path('article/',views.article,name='article'),
    path('customer/',views.customer,name='customer'),


    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,
    success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),
         name='passwordchangedone'),
         
    path('password-reset/', auth_views.PasswordResetView.
         as_view(template_name='app/password_reset.html',
                 form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.
         as_view(template_name='app/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.
         as_view(template_name='app/password_reset_confirm.html',
                 form_class=MySetPasswordForm),
         name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.
         as_view(template_name='app/password_reset_complete.html'),
         name='password_reset_complete'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
