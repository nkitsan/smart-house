from django.http import HttpResponse
from django.shortcuts import render

from climatecontroller.libs.managers import request_manager


def sensors(request, data):
	request_manager.post_data(data)
	return HttpResponse()