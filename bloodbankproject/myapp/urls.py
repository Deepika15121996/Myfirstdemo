from multiprocessing.spawn import import_main_path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addBB',views.AddBloodBank.as_view(),name="addBB"),
    path('showBBlist',views.showList,name="showBBlist"),
    path('updbb/<id>',views.UpdateBloodBank.as_view(),name="updbb"),
    path('delbb/<id>',views.DeleteBloodBank.as_view(),name="delbb"),
    path('addD',views.AddDonor.as_view(),name="addD"),
    path('showDNlist',views.showList,name="showDNlist"),
    path('upddonor/<id>',views.UpdateDonor.as_view(),name="upddonor"),
    path('deld/<id>',views.DeleteDonor.as_view(),name="deld"),
    path('addR',views.AddReceiver.as_view(),name="addR"),
    path('showRlist',views.showList,name="showRlist"),
    path('updreceiver/<id>',views.UpdateReceiver.as_view(),name="updreceiver"),
    path('delr/<id>',views.DeleteReceiver.as_view(),name="delr"),
    path('search',views.Search.as_view(),name="search"),
    path('login',views.Logins.as_view(),name="login"),
    path('logout',views.logouts,name="logout"),
    path('register',views.Registration.as_view(),name="register"),
    path('addcmp',views.AddComplaint.as_view(),name="addcmp"),
    path('showcmplist',views.showList,name="showcmplist")
    
    

]
