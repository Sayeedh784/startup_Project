from django.urls import path
from .import views
from .views import *
from .form import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('register/',views.register, name='register'),
    path('pricing/',views.pricing,name="pricing"),
    path('customer_register/',views.customer_register, name='customer_register'),
    path('startup_register/',views.startup_register, name='startup_register'),
    path('investor_register/',views.investor_register, name='investor_register'),
#     path('user_profileForm/<str:pk>/', views.userProfileForm, name='user-form'),
    path('startup-form/<int:pk>/',views.StartUpdateView.as_view(),name='startup-form'),
    path('investor-form/<int:pk>/',views.InvestorUpdateView.as_view(),name='investor-form'),
    path('customer-form/<int:pk>/',views.CustomerUpdateView.as_view(),name='customer-form'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('startup-profile/<int:pk>/', views.startup_profile, name='startup-profile'),
    path('submit_review/<int:startup_id>/',views.submit_review, name='submit_review'),
    path('investor_submit_review/<int:investor_id>/',views.investor_submit_review, name='investor_submit_review'),
    path('startup_home/',views.startup_home,name='startup_home'),
    path('investor-profile/<int:pk>/',views.investor_profile, name='investor-profile'),
    path('investor_home/',views.investor_home,name='investor_home'),
    path('search_list/',views.search_list,name="search_list"),
    path('article/',views.article,name='article'),
    path('customer_profile/<int:pk>/',views.customer_profile,name='customer_profile'),
    path('customer_home/',views.customer_home,name='customer_home'),

    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/',CreateMessage.as_view(), name='create-message'),
    path('notifiaction/<int:notification_pk>/thread/<int:object_pk>/',views.ThreadNotification.as_view(),name="thread_notification"),


    path('notification/<int:notification_pk>/profile/<int:profile_pk>',views.FollowNotification.as_view(),name="folllow-notification"),
    path('notification/<int:notification_pk>/thread/<int:object_pk>',
         ThreadNotification.as_view(), name='thread-notification'),
    path('notification/delete/<int:notification_pk>',
         RemoveNotification.as_view(), name='notification-delete'),

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
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
