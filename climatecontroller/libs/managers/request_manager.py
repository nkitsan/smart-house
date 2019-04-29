from django.utils import timezone
from datetime import datetime, timedelta

from climatecontroller.libs.managers import (humidity_manager, 
											 temperature_manager, 
											 carbondioxide_manager)
from climatecontroller.libs.parsers import request_parser
from climatecontroller.libs.helpers import params_helper


def save_sensors_data(data):
	time = datetime.now(tz=timezone.utc)

	if params_helper.temperature in data:
		temperature_manager.create_temperature(data[params_helper.temperature], time)

	if params_helper.humidity in data:
		humidity_manager.create_humidity(data[params_helper.humidity], time)

	if params_helper.carbondioxide in data:
		carbondioxide_manager.create_carbondioxide(data[params_helper.carbondioxide], time)