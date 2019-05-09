from django.urls import path
from . import views

urlpatterns = [
    path('sensors/<data>', views.sensors, name='sensors'),
    path('temperatures', views.temperature_view, name='temperature_view'),
    path('humidities', views.humidity_view, name='humidity_view'),
    path('carbondioxides', views.carbondioxide_view, name='carbondioxide_view'),
]
