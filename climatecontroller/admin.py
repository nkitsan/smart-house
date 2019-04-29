from django.contrib import admin
from .models import HumidityController, TemperatureController, CarbonDioxideController

admin.site.register(HumidityController)
admin.site.register(TemperatureController)
admin.site.register(CarbonDioxideController)