from django.contrib import admin
from django.urls import path
from map.views import mapa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapa, name='mapa'),
]
