"""Vignan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from SampleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('demo/',views.demo),
    path('msg/<str:name>/',views.mesg),
    path('info/<str:name>/<int:num>/',views.data),
    path('table/<int:n>/',views.table),
    path('dhtml/',views.dhtml),
    path('details/<str:name>/<int:n>/',views.details),
    path('scss/',views.scss),
    path('login/',views.login),
    path('BasicApp/',include('BasicApp.urls')),
    path('crud/',include('CrudApp.urls')),
]