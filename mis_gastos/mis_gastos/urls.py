from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billetera/',include('billetera.urls')),
    path('ahorros/',include('ahorros.urls')),
    path('home/',include('home.urls')),
]
