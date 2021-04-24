"""managesys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login,name="login"),
    path('',views.index,name="index"),
    path('addevents', views.addevents, name="addevents"),
    path('homeuser/<str:username>', views.homeuser, name="homeuser"),
    path('homeguard/<str:username>', views.homeguard, name="homeguard"),
    path('homeadmin', views.homeadmin, name="homeadmin"),
    path('sign_up',views.signup, name="signup"),
    path('user_reg',views.userreg, name="userreg"),
    path('guard_reg',views.guardreg, name="guardreg"),
    path('lpd/<str:username>',views.lpd, name="lpd"),
    path('complainbox/<str:username>',views.complainbox, name="complainbox"), 
    path('complainboxg/<str:username>',views.complainboxg, name="complainboxg"),  
    path('maintainpay/<str:username>',views.maintainpay, name="maintainpay"),
    path('rentpay/<str:username>',views.rentpay, name="rentpay"),
    path('addguest/<str:username>', views.addguest, name="addguest"),
    path('profile/<str:username>', views.profile, name="profile"),
    path('residentd', views.residentd, name="residentd"),
    path('guardd', views.guardd, name="guardd"),
    path('rentd', views.rentd, name="rentd"),
    path('maind', views.maind, name="maind"),
    path('cdetail', views.cdetail, name="cdetail"),
    path('rec/<str:username>', views.rec, name="rec"),
    path('eventd/<str:username>', views.eventd, name="eventd"),
    path('guestd', views.guestd, name="guestd"),
    path('uge/<str:username>', views.uge, name="uge"),
    path('help/<str:username>', views.help, name="help"),    
    path('chat/<str:username>', views.chat_view, name='chat_view'),
    path('chat/<str:sender>/<str:receiver>/', views.message_view, name='chat'),
    path('api/messages/<str:sender>/<str:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
]
