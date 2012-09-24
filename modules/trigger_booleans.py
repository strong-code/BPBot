decision = True
links = True
quote = True
weather = True
zumba = True
rude = True
response = True
conversion = True

loaded = [decision, links, quote, weather, zumba, rude, response, conversion]

def toggleTrigger(triggerName):
	global decision
	global links
	global quote
	global weather
	global zumba
	global rude
	global response
	global conversion

	if triggerName == 'decision':
		if decision:
			decision = False
			loaded.remove(decision)
			return 'Decision trigger is disabled'
		else:
			decision = True
			loaded.append(decision)
			return 'Decision trigger is enabled'
	elif triggerName == 'links':
		if links:
			links = False
			loaded.remove(links)
			return 'Links trigger is disabled'
		else:
			links = True
			loaded.append(links)
			return 'Links trigger is enabled'
	elif triggerName == 'quote':
		if quote:
			quote = False
			loaded.remove(quote)
			return 'Quote trigger is disabled'
		else:
			quote = True
			loaded.append(quote)
			return 'Quote trigger is enabled'
	elif triggerName == 'weather':
		if weather:
			weather = False
			loaded.remove(weather)
			return 'Weather trigger is disabled'
		else:
			weather = True
			loaded.append(weather)
			return 'Weather trigger is enabled'
	elif triggerName == 'zumba':
		if zumba:
			zumba = False
			loaded.remove(zumba)
			return 'Zumba trigger is disabled'
		else:
			zumba = True
			loaded.append(zumba)
			return 'Zumba trigger is enabled'
	elif triggerName == 'rude':
		if rude:
			rude = False
			loaded.remove(rude)
			return 'Rude trigger is disabled'
		else:
			rude = True
			loaded.append(rude)
			return 'Rude trigger is enabled'
	elif triggerName == 'response':
		if response:
			response = False
			loaded.remove(response)
			return 'Response trigger is disabled'
		else:
			response = True
			loaded.append(response)
			return 'Response trigger is enabled'
	elif triggerName == 'conversion':
		if conversion:
			conversion = False
			loaded.remove(conversion)
			return 'Conversion trigger is disabled'
		else:
			conversion = True
			loaded.append(conversion)
			return 'Conversion trigger is enabled'
	else:
		return 'Incorrect trigger name, did you spell that correctly?'