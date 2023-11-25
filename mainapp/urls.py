from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.specialists, name='index'),
   path('<int:pk>/', mainapp.specialist, name='specialist'),
]

#
# from django.contrib import admin
# from mainapp import views as mainapp
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import include
#
# urlpatterns = [
#     path('', mainapp.main, name='main'),
#
#     path('specialists/', include('mainapp.urls', namespace='mainapp')),
#     # path('specialists/tatyana/', mainapp.specialist_tatyana, name='specialist_tatyana'),

#     # path('specialist/mariya/', mainapp.specialist_mariya, name='specialist_mariya'),
#     # path('specialist/lidiya/', mainapp.specialist_lidiya, name='specialist_lidiya'),
#     # path('specialist/anastasiya/', mainapp.specialist_anastasiya, name='specialist_anastasiya'),
#
#     path('contacts/', mainapp.contacts, name='contacts'),
#     path('admin/', admin.site.urls),
# ]
