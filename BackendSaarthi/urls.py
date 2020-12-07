"""BackendSaarthi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Saarthi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login,name="login"),
    path('register/',Register,name="register"),
    path('enter_url/',Enter_Url,name="enter_url"),
    path('show_url/',Show_Url,name="show_url"),
    path('logout/',Logout,name="logout"),
    path('show_web/<int:q_id>/',Show_Web,name="show_web"),

]
