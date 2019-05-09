from django.utils import timezone
from datetime import datetime, timedelta

import requests

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

def change_controller_state(ip, gpio, value):
	if value == 1 or value == 0:
		requests.get('http://%(ip)s/control?cmd=GPIO,%(gpio)s,%(value)s' %
					 (ip, gpio, value))

def get_controller_state(ip, gpio):
	response = requests.get('http://%(ip)s/control?cmd=Status,GPIO,%(gpio)s' %
							(ip, gpio, value)).json()

	return response['state']