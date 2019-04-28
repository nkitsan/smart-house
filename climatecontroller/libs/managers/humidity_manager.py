from django.utils import timezone
from datetime import datetime, timedelta

from climatecontroller.models import Humidity


def create_humidity(value, time):
	Humidity.objects.create(value=value, time=time)

def get_humidities():
	humidities = Humidity.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)
	result = [] 

	for humidity in humidities:
		if time_now - humidity.time <= delta_time:
			result.append(humidity)

	return result

def delete_humidity(humidity):
	Humidity.objects.filter(id=humidity.id).delete()

def delete_obsolete_data():
	humidities = Humidity.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)

	for humidity in humidities:
		if time_now - humidity.time >= delta_time:
			delete_humidity(humidity)
