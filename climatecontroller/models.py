from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class HumidityController(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	preffered_value = models.FloatField(validators=[MinValueValidator(30.0), MaxValueValidator(60.0)], default=30.0)
	control_mode = models.BooleanField(default=True)
	delta = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=1.0)
	
class TemperatureController(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	preffered_value = models.FloatField(validators=[MinValueValidator(16.0), MaxValueValidator(30.0)], default=22.0)
	control_mode = models.BooleanField(default=True)
	delta = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=1.0)

class CarbonDioxideController(models.Model):
	controller_ip = models.GenericIPAddressField()
	controller_gpio = models.PositiveSmallIntegerField(blank=False, null=False)
	control_mode = models.BooleanField(default=True)
	max_value = models.FloatField(validators=[MinValueValidator(2000.0), MaxValueValidator(10000.0)], default=10000.0)
	min_value = models.FloatField(validators=[MinValueValidator(2000.0), MaxValueValidator(10000.0)], default=2000.0)
						
class Humidity(models.Model):
	time = models.DateTimeField()
	value = models.FloatField()

class Temperature(models.Model):
	time = models.DateTimeField()
	value = models.FloatField()
	
class CarbonDioxide(models.Model):
	time = models.DateTimeField()
	value = models.FloatField()