from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio_dashboard, name='inicio_dashboard'),
]