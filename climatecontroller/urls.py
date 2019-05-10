from django.urls import path
from . import views

urlpatterns = [
    path('sensors/<data>', views.sensors, name='sensors'),

    path('temperatures', views.temperature_view, name='temperature_view'),
    path('humidities', views.humidity_view, name='humidity_view'),
    path('carbondioxides', views.carbondioxide_view, name='carbondioxide_view'),

    path('temperatures/state', views.change_temperature_controller_state, name='change_temperature_controller_state'),
    path('humidities/state', views.change_humidity_controller_state, name='change_humidity_controller_state'),
    path('carbondioxides/state', views.change_carbondioxide_controller_state, name='change_carbondioxide_controller_state'),

    path('temperatures/mode', views.change_temperature_controller_mode, name='change_temperature_controller_mode'),
    path('humidities/mode', views.change_humidity_controller_mode, name='change_humidity_controller_mode'),
    path('carbondioxides/mode', views.change_carbondioxide_controller_mode, name='change_carbondioxide_controller_mode'),
]
