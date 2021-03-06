"""djangoForms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home,name="home"),

    path("addBook/",views.add_book,name="add_book"),
    path("books/",views.books,name="books"),
    path("update/<int:book_no>",views.update,name="update"),
    path("delete/<int:book_no>",views.delete,name="delete"),

    path('contactUs/',views.contact_us,name="contact_us"),
]
