from django.http import HttpResponse
from django.shortcuts import render

from climatecontroller.libs.managers import (request_manager, 
											 controller_manager,
											 temperature_manager,
											 humidity_manager,
											 carbondioxide_manager)
from climatecontroller.libs.parsers import request_parser


def sensors(request, data):
	params = request_parser.string_to_dict(data)
	request_manager.save_sensors_data(params)
	controller_manager.control_climate(params)
	return HttpResponse()

def temperature_view(request):
	data = request_parser.objects_to_json(temperature_manager.get_temperatures())
	mode = temperature_manager.get_mode()
	state = controller_manager.get_temperature_controller_state()
	return render(request, 'climatecontroller/temperature.html', {'data': data,
														   'mode': mode,
														   'state': state})

def humidity_view(request):
	data = request_parser.objects_to_json(humidity_manager.get_humidities())
	mode = humidity_manager.get_mode()
	state = controller_manager.get_humidity_controller_state()
	return render(request, 'climatecontroller/humidity.html', {'data': data,
														   'mode': mode,
														   'state': state})

def carbondioxide_view(request):
	data = request_parser.objects_to_json(carbondioxide_manager.get_carbondioxides())
	mode = carbondioxide_manager.get_mode()
	state = controller_manager.get_carbondioxide_controller_state()
	return render(request, 'climatecontroller/carbondioxide.html', {'data': data,
														   'mode': mode,
														   'state': state})
