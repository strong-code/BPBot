from irc_commands import *
from ignore import *
import re

_triggers = []

#cycle through all triggers and, if loaded, deliver the
#appropriate response to the chan
def findTriggers(s, user, type, chan, msg):
	if isIgnored(user):
		return #don't check for triggers from ignored users
	else:
		print '<<< MSG IS: ' + str(msg)
		if msg == 'quit':
			quit(s, 'Leaving!')
			return
		if msg == 'IL':
			sendMessage(s, showList(s))
			return
		if re.match('\.iu\s(.*)', str(msg)):
			hostmask = re.match('\.iu\s(.*)', str(msg)).group(1)
			sendMessage(s, ignoreUser(hostmask))

#This should be fixed so it send to different parsing functions
#depending on elements in line[]
def parseLine(s, currLine):
	line = currLine.split()
	if len(line) >= 4 and line[1] == 'PRIVMSG': #user message to channel
		user = line[0]
		type = line[1]
		chan = line[2]
		msg = ' '.join(line[3:])
		findTriggers(s, user, type, chan, msg[1:])
	if len(line) == 2: #most likely a ping, or server alert
		if line[0] == 'PING':
			pong(s)

	# There are still a few other types of messages we will get
	# from the server, but this will be done via trial and error
	# I guess?