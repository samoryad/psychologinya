"""psychologinya URL Configuration

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
from django.urls import path
from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),

    path('specialists/', mainapp.specialists, name='specialists'),
    path('specialists/all/', mainapp.specialists_all, name='specialists_all'),
    path('specialists/svetlana/', mainapp.specialists_svetlana, name='specialists_svetlana'),
    path('specialists/mariya/', mainapp.specialists_mariya, name='specialists_mariya'),
    path('specialists/lidiya/', mainapp.specialists_lidiya, name='specialists_lidiya'),
    path('specialists/anastasiya/', mainapp.specialists_anastasiya, name='specialists_anastasiya'),

    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]
