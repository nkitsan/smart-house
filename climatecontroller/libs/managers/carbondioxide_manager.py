from django.utils import timezone
from datetime import datetime, timedelta

from climatecontroller.models import CarbonDioxide


def create_carbondioxide(value, time):
	CarbonDioxide.objects.create(value=value, time=time)

def get_carbondioxides():
	carbondioxides = CarbonDioxide.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)
	result = [] 

	for carbondioxide in carbondioxides:
		if time_now - carbondioxide.time <= delta_time:
			result.append(carbondioxide)

	return result

def delete_carbondioxide(carbondioxide):
	CarbonDioxide.objects.filter(id=carbondioxide.id).delete()

def delete_obsolete_data():
	carbondioxides = CarbonDioxide.objects.all()
	time_now = datetime.now(tz=timezone.utc)
	delta_time = timedelta(days=1)

	for carbondioxide in carbondioxides:
		if time_now - carbondioxide.time >= delta_time:
			delete_carbondioxide(carbondioxide)