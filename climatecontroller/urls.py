from django.urls import path
from . import views

urlpatterns = [
    path('sensors/<data>', views.sensors, name='sensors'),
    path('temperatures', views.temperature_view, name='temperature_view'),
]
