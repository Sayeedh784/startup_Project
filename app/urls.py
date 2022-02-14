from django.urls import path
from .import views
from .views import *
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
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('startup-profile/<int:pk>/', views.startup_profile, name='startup-profile'),
    path('submit_review/<int:startup_id>/',views.submit_review, name='submit_review'),
    path('investor_submit_review/<int:investor_id>/',views.investor_submit_review, name='investor_submit_review'),
    path('startup_home/',views.startup_home,name='startup_home'),
    path('investor-profile/<int:pk>/',views.investor_profile, name='investor-profile'),
    path('investor_home/',views.investor_home,name='investor_home'),
    path('search_list/',views.search_list,name="search_list"),
    path('article/',views.article,name='article'),
    path('customer_profile/<int:pk>',views.customer_profile,name='customer_profile'),
    path('customer_home/',views.customer_home,name='customer_home'),

    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/',CreateMessage.as_view(), name='create-message'),

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
