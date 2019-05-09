from django.http import HttpResponse
from django.shortcuts import render

from climatecontroller.libs.managers import (request_manager, 
											 controller_manager)
from climatecontroller.libs.parsers import request_parser


def sensors(request, data):
	params = request_parser.string_to_dict(data)
	request_manager.save_sensors_data(params)
	controller_manager.control_climate(params)
	return HttpResponse()