"""ReviewProj URL Configuration

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
import mainapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.index, name="index"),
    path('read/<int:post_id>', mainapp.views.read, name='read'),
    path('create/', mainapp.views.create, name="create"),
    path('update/<int:post_id>', mainapp.views.update, name="update"),
    path('delete/<int:post_id>',mainapp.views.delete,name='delete'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
]