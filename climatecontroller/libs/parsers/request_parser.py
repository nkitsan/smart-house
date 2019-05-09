from datetime import datetime


TIME_PATTERN = '%Y-%m-%d %H:%M'

def string_to_dict(str):
	result = {}
	pairs = str.split('&')

	for pair in pairs:
		param, value = pair.split('=')
		result.update({param : value})

	return result

def objects_to_json(objects):
	data = []

	for obj in objects:
		data.append([obj.time.strftime(TIME_PATTERN), obj.value])
	
	return data
