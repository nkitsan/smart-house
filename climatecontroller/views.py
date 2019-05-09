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
	return render(request, 'climatecontroller/base.html', {'temperatures': data})
