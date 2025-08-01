from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #pagina inicial+ (João Pedro)
    path('', views.index, name='index'), 
    path('saiba-mais/', views.saiba_mais, name='saiba_mais'),
]
