from irc_commands import *

_triggers = []

#cycle through all triggers and, if loaded, deliver the
#appropriate response to the chan
def findTriggers(s, line):
	if line == 'quit':
		quit(s, 'Leaving!')
	sendMessage(s, 'your message was: ' + line)

#This should be fixed so it send to different parsing functions
#depending on elements in line[]
def parseLine(s, currLine):
	line = currLine.split()
	try:
		if line[0] == 'PING':
			pong(s)
		if len(line) >= 4 and line[1] == 'PRIVMSG': #someone is talking
			findTriggers(s, line[3][1:].strip('\r\n'))
	except IndexError:
		pass


