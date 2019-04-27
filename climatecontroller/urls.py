from django.urls import path
from . import views

urlpatterns = [
    path('sensors/<data>', views.sensors, name='sensors'),
]