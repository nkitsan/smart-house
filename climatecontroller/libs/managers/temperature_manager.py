from django.utils import timezone
from datetime import datetime, timedelta

from climatecontroller.models import Temperature


def create_temperature(value, time):
	Temperature.objects.create(value=value, time=time)

def get_temperatures():
	temperatures = Temperature.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)
	result = [] 

	for temperature in temperatures:
		if time_now - temperature.time <= delta_time:
			result.append(temperature)

	return result

def delete_temperature(temperature):
	Temperature.objects.filter(id=temperature.id).delete()

def delete_obsolete_data():
	temperatures = Temperature.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)

	for temperature in temperatures:
		if time_now - temperature.time >= delta_time:
			delete_temperature(temperature)