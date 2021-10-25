from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('donorform/',views.donorform,name='donorform'),
    path('donorlist/',views.donorlist,name='donorlist'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('donorinfo/<int:donor_id>',views.donorinfo,name='donorinfo'),
    path('donorupdate/<int:donor_id>',views.donorupdate,name='donorupdate'),
    path('donordelete/<int:donor_id>',views.donordelete,name='donordelete'),
    
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

]
