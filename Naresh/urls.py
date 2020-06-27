"""Naresh URL Configuration

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
from Me.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login,name="login"),
    path('logout/',Logout,name="logout"),
    path('',Index,name="index"),
    path('userDetailsForm/',Add_User_Details,name="userDetails"),
    path('editUserDetails/',Edit_User_Details,name="editUserDetails"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
