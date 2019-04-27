from django.contrib import admin
from .models import HumiditySensor, TemperatureSensor, CarbonDioxideSensor

admin.site.register(HumiditySensor)
admin.site.register(TemperatureSensor)
admin.site.register(CarbonDioxideSensor)