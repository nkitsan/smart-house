from django.urls import path
from . import views

urlpatterns = [
    path('sensers/<data>', views.sensers, name='sensers'),
]