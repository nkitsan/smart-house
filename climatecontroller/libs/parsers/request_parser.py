def string_to_dict(str):
	result = {}
	pairs = str.split('&')

	for pair in pairs:
		param, value = pair.split('=')
		result.update({param : value})

	return result