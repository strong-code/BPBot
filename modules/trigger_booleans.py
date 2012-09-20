decision = True
links = True
quote = True
weather = True
zumba = True
rude = True

def toggleTrigger(triggerName):
	global decision
	global links
	global quote
	global weather
	global zumba
	global rude

	if triggerName == 'decision':
		print '>>>DECIDE IS SET TO ' + str(decision)
		if decision:
			decision = False
			return 'Decision trigger is disabled'
		else:
			decision = True
			return 'Decision trigger is enabled'
	elif triggerName == 'links':
		if links:
			links = False
			return 'Links trigger is disabled'
		else:
			links = True
			return 'Links trigger is enabled'
	elif triggerName == 'quote':
		if quote:
			quote = False
			return 'Quote trigger is disabled'
		else:
			quote = True
			return 'Quote trigger is enabled'
	elif triggerName == 'weather':
		if weather:
			weather = False
			return 'Weather trigger is disabled'
		else:
			weather = True
			return 'Weather trigger is enabled'
	elif triggerName == 'zumba':
		if zumba:
			zumba = False
			return 'Zumba trigger is disabled'
		else:
			zumba = True
			return 'Zumba trigger is enabled'
	elif triggerName == 'rude':
		if rude:
			rude = False
			return 'Rude trigger is disabled'
		else:
			rude = True
			return 'Rude trigger is enabled'
	else:
		return 'Incorrect trigger name, did you spell that correctly?'