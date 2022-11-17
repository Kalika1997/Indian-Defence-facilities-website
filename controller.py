from django.urls import path
from sms.views import home,  Emp_signup, aboutus
from . import views
app_name='sms'

from django.conf.urls import *
from django.contrib.auth import views as auth_views

urlpatterns = [



    path('',home,name='home'),
path('school/rules',views.rules,name='rules'),

path('contact',views.contact,name='contact'),
path('galary',views.galary,name='gallary'),
path('school/admission',views.admission,name='admission'),
path('user',views.User_manage,name='user'),
path('about',views.about_hospital,name='aboutus'),
path('hospital/medicalprocess',views.medical,name='medical'),
path('cant/home',views.School_home,name='school_home'),
path('bookings',views.mybooking,name='booking'),
path('cant/school/<slug>',views.School,name='school'),
path('cant/school/detail/<slug>',views.School_details,name='school_detail'),
path('melitory/hospital',views.armyHospital,name='hospital'),
path('canteen',views.Canteen_home,name='canteen'),
path('canteen/checkout',views.checkout,name='checkout'),
path('admin/home',views.Admin_home,name='admin_home'),
    path('login/', views.Emp_login.as_view(), name='login'),
path('login/admin', views.Admin_login.as_view(), name='admin_login'),
path('logout', views.logoutpage.as_view(), name='logout'),
path('reset/<uidb64>/<token>/',home, name='email'),

path('employee/signup',Emp_signup.as_view(),name='emp_signup'),

path('edit/user/<int:pk>',views.Edit_User.as_view(), name='edit_user'),

path('profile',views.profile,name='profile'),
path('profile/add',views.Add_profile.as_view(), name='add_profile'),


]
'''
path('accounts/login/',auth_views.LoginView,name='login'),

path('accounts/password_change/',auth_views.PasswordChangeView,name='password_change'),
path('accounts/password_change/done/',auth_views.PasswordChangeDoneView, name='password_change_done'),
path('accounts/password_resets/',auth_views.PasswordResetView, name='password_reset'),
path('accounts/password_reset/done/',auth_views.PasswordResetDoneView, name='password_reset_done'),
path('accounts/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
path('accounts/reset/done/',auth_views.PasswordResetCompleteView, name='password_reset_complete'),

'''