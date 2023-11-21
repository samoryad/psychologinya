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
    path('specialists/tatyana/', mainapp.specialist_tatyana, name='specialist_tatyana'),
    path('specialist/svetlana/', mainapp.specialist_svetlana, name='specialist_svetlana'),
    path('specialist/mariya/', mainapp.specialist_mariya, name='specialist_mariya'),
    path('specialist/lidiya/', mainapp.specialist_lidiya, name='specialist_lidiya'),
    path('specialist/anastasiya/', mainapp.specialist_anastasiya, name='specialist_anastasiya'),

    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]
