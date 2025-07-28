from django.urls import path
from .import views

urlpatterns=[
    path('',views.landingpageview,name='home'),  # Root path for homepage
    path('first',views.firstpageview,name='fisrt'),
    path('landing',views.landingpageview,name='landing'),
    path('pricing',views.pricingpageview,name='pricing'),
    path('contact',views.contactpage,name='contact'),
    path('pricing2',views.pricingpageview2,name='pricing2'),
    path('index',views.indexpageview,name='index'),
    path('student',views.studentview,name='student'),
    path('register',views.registerview,name='register'),
    path('login', views.loginview, name='login'),
    #DASHBOARD PAGE
    path('dashboard',views.dashboardview,name='dashboard'),
]