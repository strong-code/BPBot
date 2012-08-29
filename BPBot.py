
'''
An IRC robot for #fit on Rizon's IRC network. Meant to help with
various functions and humor.

Created by Colin Lindsay

https://clindsay107@github.com/clindsay107/BPBot.git
'''

import ssl, socket, re, sys
from modules import *

#variables for server connection
server = config.server
chan = config.chan
port = config.port
nick = config.nick
password = config.password
SSL = config.SSL
inChan = False

if SSL:
	s = wrapSSL(s)
else: #create the network socket and connect
	s = socket.socket()

s.connect((server, port))
s.sendall('USER ' + nick + ' '+ nick + ' ' + nick + ' :BPBot\n')
setNick(s)
identify(s)

if not setUp():#do database setup
	print '>>>Problem setting up database!'

#Receive input until we are in the channel
while not inChan:
	line = readLine(s)
	print line
	line = line.split() #parse the line for codes
	try:
		if len(line) <= 1: #ignore blank lines, should be handled better...
			pass
		if line[0] == 'ERROR': #should log this
			print '>>>ERROR CONNECTING, CONNECTION TIMEOUT'
			s.close()
			break
		if line[1] == '353': #we are in chan, set to true
			inChan = True
		if line[1] == '433': #NEEDS TO BE FIXED!!!
			ghost(s)
			identify(s)
			joinChan(s)
		if line[1] == '376':
			joinChan(s)
	except IndexError:
		pass

while inChan:
	line = readLine(s)
	print line
	parseLine(s, line)