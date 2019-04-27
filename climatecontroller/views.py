from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def sensors(request, data):
	print(data)
	return HttpResponse()