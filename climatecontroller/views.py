from django.http import HttpResponse
from django.shortcuts import render

from climatecontroller.libs.managers import request_manager
from climatecontroller.libs.parsers import request_parser


def sensors(request, data):
	request_manager.save_sensors_data(request_parser.string_to_dict(data))
	return HttpResponse()