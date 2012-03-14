'''
An IRC bot written in Python for #fit on Rizon.
Helps with conversions and 1RM estimates, as well
as a few other things.

v0.5 3/13/12 - now with 100% more SSL!
'''

import ssl, socket, re, random

server = "irc.rizon.net"
chan = '#fit'
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
	ircsock.send("PRIVMSG " + chan + " :I'm leaving\n") #Send our final goodbyes to the channel
	randomNick = 'nwoihgwnv' + str(random.randint(0,100)) #disown our nick to something random
	ircsock.send("NICK " + randomNick)
	ircsock.close() 

def input(listed):
	lift = '' #if the values never change, tell the user they misused the syntax
	weight = ''
	typesOfLifts = ['deadlift', 'benchpress', 'ohp', 'squat']
	for l in typesOfLifts:
		if (listed[1] == l):
			lift = listed[1]

	if re.search(r'\d+[lk][bg]', listed[2]): #still can log mathematical functions, fix this
		weight = listed[2]

	if (lift == '' or weight == ''):
		print listed[2]
		ircsock.send("PRIVMSG " + chan + " :Incorrect format, use !log deadlift 225lb\n")
	else:
		ircsock.send("PRIVMSG " + chan + " :Logging " + weight + " for your new " + lift + " record\n")
	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
ircsock = ssl.wrap_socket(s)
ircsock.send("USER " + nick + " " + nick + " " + nick + " :BPBot\n")
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
		try:
			logReg = re.compile('\!log\s.+')
			line = logReg.search(line).group(0)
			listed = re.split('\s', line)
			input(listed)
		except AttributeError:
			ircsock.send("PRIVMSG " + chan + " :You need to supply arguments!\n")
		except IndexError:
			ircsock.send("PRIVMSG " + chan + " :You need to supply ALL arguments!\n")
			
