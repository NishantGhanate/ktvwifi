from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.homePage , name ='homePage'),
    path('pricing', views.pricing , name='pricing'),
    path('contactus', views.contactus),
    path('faq', views.faq),

    path('signup', views.signupPage , name = 'signupPage'),
    path('login', views.loginPage , name = 'loginPage'),
    path('logout', views.logoutUser , name = 'logoutUser'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='ktvwifi/reset_password.html'), name='reset_password'),
    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name='ktvwifi/reset_password_done.html') , name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='ktvwifi/password_reset_confirm.html') , name='password_reset_confirm'),
    path('resest_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='ktvwifi/resest_password_complete.html') , name='password_reset_complete'),

    path('complaints', views.userComplaints , name = 'userComplaints'),
    path('settings', views.userSettings , name = 'userSettings'),
    
    path('dashboard/home', views.adminHome , name = 'dashboard'),
    path('dashboard/customers', views.adminCustomers , name = 'customers'),
    path('dashboard/complaints', views.adminComplaints , name = 'complaints'),
    path('dashboard/contacts', views.adminContact , name = 'contacts'),
    path('dashboard/internetplans', views.adminPlans , name = 'plans'),
    path('dashboard/internetplans/delete', views.adminPlansDelete , name = 'deletePlan'),
]
