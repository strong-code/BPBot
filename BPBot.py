'''
An IRC bot written in Python for #fit on Rizon.
Helps with conversions and 1RM estimates, as well
as a few other things.

v0.5 3/5/12 - now with 100% more SSL!
'''

import ssl, socket, re

server = "irc.rizon.net"
chan = '#bptest'
port = 6697
nick = "BPBot"

def ping():
	ircsock.send("Pong :pingis\n")

def sendMessage():
	ircsock.send("PRIVMSG " + chan + " :" + msg + "\n")

def joinChan(chan):
	ircsock.send("JOIN " + chan + "\n")

def hello():
	ircsock.send("PRIVMSG " + chan + " : hello\n")

def logoff():
	ircsock.send("PRIVMSG " + chan + " :Leaving\n") #Send our final goodbyes to the channel
	ircsock.send("NICK fefg24g4425") #disown our nick to something random
	ircsock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
ircsock = ssl.wrap_socket(s)
ircsock.send("USER " + nick + " " + nick + " " + nick + " :this is a test\n")
ircsock.send("NICK " + nick + "\n")

joinChan(chan)

while 1:
	line = ircsock.recv(1000)
	line = line.strip('\n\r')
	print(line)

	if line.find("PING :") != -1: #respond to Ping requests
		ping()

	if line.find(":Hello " + nick) != -1: #respond to a simple Hello
		hello()

	if line.find("PRIVMSG " + nick + " :logoff") != -1: #logoff and close socket connection when given the kill command
		logoff()

	if line.find(":!log") != -1:
		messageToLog = re.compile('\!log\s.+', re.IGNORECASE)
		string = messageToLog.search(line).group(1)
		print string

#f = open('test.txt')
#f.written