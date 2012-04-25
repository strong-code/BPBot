def logoff():
	randomNick = nick + str(random.randint(0,100)) #disown our nick to something random
	logoffMessage = '/part\n'
	return logoffMessage