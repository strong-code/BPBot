from modules import config
import log

#some variables we will need
chan = config.chan
nick = config.nick
password = config.password
holder = []
buffer = ''
admins = config.admins

#join chan
def joinChan(s):
	s.sendall("JOIN %s \n" % chan)

#set our nickname
def setNick(s):
	s.sendall("NICK %s \n" % nick)

#send identify command to NickServ
def identify(s):
	s.sendall("IDENTIFY %s \n" % password)

#attempt to ghost the current nickname
def ghost(s):
	s.sendall("/msg NickServ GHOST %s :%s \n" % (nick, password))

#send leaving message, then close socket
#Could be a LOT better
def quit(s, reason):
	sendMessage(s, reason)
	#log.closeLog()
	s.close()

#respond to PING requests
def pong(s):
	s.sendall("PONG :pingis")

#join channels we are invited to
def acceptInvite(s, inviteChan):
	s.sendall('JOIN %s \n' % inviteChan)

#use SSL connection
def wrapSSL(socket, nick, password, server):
	port = 6697
	ircsock = ssl.wrap_socket(socket)
	return ircsock

#Check if a user is admin (for BPBot, not the chan)
def isAdmin(nick):
	for user in admins:
		if user == nick:
			return True
	return False

#parse the input line by line
#TODO: separate by type, sender, hostmask, etc
def readLine(s):
	global holder
	global buffer
	while True:
		if len(holder) > 0: #if we have items in buffer, pop and return
			if holder[0] == '\n': #remove/pop blank lines
				holder.pop(0)
			else:
				return holder.pop(0)
		buffer = s.recv(1024) #buffer the input
		holder = buffer.split("\n") #split on newline

#sends a message to broadcast to the entire current channel
def sendMessage(s, message):
	try:
		message.strip()
		s.sendall('PRIVMSG ' + chan + ' :' + message + '\n')
	except AttributeError:
		#if somehow something else gets through
		#should really be logged
		pass