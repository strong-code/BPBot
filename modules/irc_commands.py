def logoff(message):
	return "QUIT :%s" % message

def joinChan(chan):
	return "JOIN %s" % chan

def ping():
	return "PONG :pingis"

def identify(nick, password):
	return "NickServ IDENTIFY %s" % password

def setUser(nick):
	return "USER %s %s %s" + " :BPBot\n" %(nick, nick, nick)

def setNick(nick):
	return "NICK %s" % nick + '\n'