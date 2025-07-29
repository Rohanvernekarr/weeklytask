from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

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
    path('logout', views.logoutview, name='logout'),
    #DASHBOARD PAGE
    path('dashboard',views.dashboardview,name='dashboard'),
    path('api/', include(router.urls)),

    
]