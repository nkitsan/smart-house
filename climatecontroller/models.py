from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HumiditySensor(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	preffered_value = models.FloatField(validators=[MinValueValidator(30.0), MaxValueValidator(60.0)], default=30.0)
	control_mode = models.BooleanField(default=True)
	state = models.BooleanField(default=False)
	
class TemperatureSensor(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	preffered_value = models.FloatField(validators=[MinValueValidator(20.0), MaxValueValidator(25.0)], default=22.0)
	control_mode = models.BooleanField(default=True)
	state = models.BooleanField(default=False)

class CarbonDioxideSensor(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	control_mode = models.BooleanField(default=True)
	state = models.BooleanField(default=False)
						
class Humidity(models.Model):
	time = models.DateTimeField()
	value = models.FloatField()

class Temperature(models.Model):
	time = models.DateTimeField()
	value = models.FloatField()
	
class CarbonDioxide(models.Model):
	time= models.DateTimeField()
	value = models.FloatField()