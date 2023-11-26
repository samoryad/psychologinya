from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.specialists, name='index'),
   path('<int:pk>/', mainapp.specialist, name='specialist'),
]
