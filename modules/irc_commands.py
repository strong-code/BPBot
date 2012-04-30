def logoff(message):
	return "QUIT :%s" % message

def joinChan(chan):
	return "JOIN %s" % chan

def ping():
	return "PONG :pingis"

def identify(nick, password):
	return "NickServ IDENTIFY %s" % password
