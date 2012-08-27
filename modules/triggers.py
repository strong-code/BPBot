from __init__ import *

_triggers = []

#cycle through all triggers and, if loaded, deliver the
#appropriate response to the chan
def findTriggers(s, user, nick, hostmask, type, chan, msg):
	msgList = msg.split() #this will help with finding triggers
	if isIgnored(hostmask):
		return #don't check for triggers from ignored users
	else:
		# print '<<< MSG IS: ' + str(msg)
		if type == 'INVITE':
			acceptInvite(msg[1:])
			return
		if msgList[0] == '.quote':
			sendMessage(s, searchLog(' '.join(msgList[1:])))
		# if msg[0] == ' .getmax':
		# 	sendMessage(s, return1RM(nick, msg[1].strip()))
		# if msg[0] == ' .rm':
		# 	insert1RM(nick, msg[1].strip(), msg[2].strip())
		if msg == 'quit' and isAdmin(nick): #this should be changed to some admin module
			quit(s, 'Leaving!')
			return
		if re.match('\.w\s(.*)', str(msg)):
			loc = re.match('\.w\s(.*)', str(msg)).group(1)
			sendMessage(s, currWeather(loc))
		if msg == 'IL':
			sendMessage(s, showList(s))
			return
		if re.match('\.iu\s(.*)', str(msg)):
			host = re.match('\.iu\s(.*)', str(msg)).group(1)
			sendMessage(s, ignoreUser(host, nick))
		urlFinder = re.search('(http(s)?://([^/#\s]+)[^#\s]*)(#|\\b)', msg, re.I | re.S)
		if urlFinder != None:
			sendMessage(s, isValidPage(urlFinder.group(1)))
		if msgList[0] == '.d':
			sendMessage(s, decide(str(msg)))

#split the line into logical parts
def parseLine(s, currLine):
	line = currLine.split()
	try:
		if line[1] == 'PRIVMSG':
			user = line[0]
			nick = getNick(user)
			hostmask = getHostmask(user)
			type = line[1]
			chan = line[2]
			msg = ' '.join(line[3:])
			findTriggers(s, user, nick, hostmask, type, chan, msg[1:])
			if logging:
				writeToLog(nick + ' said: ' + msg[1:])
		if line[1] == 'INVITE':
			acceptInvite(s, line[3][1:])
		if len(line) == 2: #most likely a ping, or server alert
			if line[0] == 'PING':
				pong(s)
	except IndexError:
		pass