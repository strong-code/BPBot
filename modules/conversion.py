def convert(weight):
	if 'kg' in weight:
		return kiloToPound(weight)
	else: return poundToKilo(weight)

def kiloToPound(weight):
	weight = weight.replace('kg', '').strip()
	try:
		weight = float(weight) * 2.205
		return 'Thats ' + ('%.2f' % round(weight, 2)) + 'lb'
	except:
		return

def poundToKilo(weight):
	weight = weight.replace('lb', '').strip()
	try:
		weight = float(weight) / 2.205
		return 'Thats ' + ('%.2f' % round(weight, 2)) + 'kg'
	except:
		return
