from django.contrib import admin
from django.urls import path
from api.views import bfhl_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bfhl/', bfhl_view, name='bfhl'), 
]
