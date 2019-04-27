from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def sensers(request, data):
	print(data)
	return