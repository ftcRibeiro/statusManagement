"""mysite URL Configuration

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
from projectApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('maquinas/', views.maquinas,name='maquinas'),
    path('maquinas/create', views.createMaquina, name='createMaquina'),
    path('maquinas/delete', views.deleteMaquina, name='deleteMaquina'),
    path('maquinas/update', views.updateMaquina, name='updateMaquina'),
    path('status/', views.maquinas,name='maquinas'),
    path('status/create', views.createStatus, name='createStatus'),
    path('status/delete', views.deleteStatus, name='deleteStatus'),
    path('status/update', views.updateStatus, name='updateStatus'),

]
