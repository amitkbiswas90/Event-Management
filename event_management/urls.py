from django.contrib import admin
from django.urls import path, include
from organizar.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('organizar.urls')),
]
