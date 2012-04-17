'''
An IRC bot written in Python for #fit on Rizon.
Helps with conversions and 1RM estimates, as well
as a few other things.

v0.7 4/9/12 - now with 100% more SSL!

CURRENT CHANGES:
-Voteban system (mostly) implemented
-Nutritional info lookup needs to be finished
-1RM logging possibly abandoned? Will have to come back it
'''

import ssl, socket, re, random, urllib2
from threading import Timer
from HTMLParser import HTMLParser

server = "irc.rizon.net"
chan = '#fittest'
port = 6697
nick = "BPBot"
activeVote = False
countedVotes = 0
userToKick = ''
userExists = False
userHostMask = ''

def ping():
	ircsock.send("Pong :pingis\n")

def joinChan(chan):
	ircsock.send("JOIN " + chan + "\n")

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

def findNutritionalInfo(foodItem):
	query = "http://www.livestrong.com/search/?mode=standard&search="
	foodItem = re.split(" ", str(foodItem))
	for l in foodItem:
		query += l + "+" #append each word of foodItem to the query URL

	result = urllib2.urlopen(query).read()
	if result.find('<article'):
		info = result[result.find('<article')+1:result.find('</article>')] #grab the first returned result
	info = re.split("\w>", info)
	for i in info:
		i = re.sub('<[^<]+?>', '', i)
		i = re.sub('\s+', ' ', i)
		i = re.sub('[,;]', '', i)
		i = re.sub('</spa', '', i)
		i = i.rstrip('\t\r\n\0')
		nutrinfo = ''
		print 'i is: ' + i + ' and nutrinfo is ' + nutrinfo
		if i.find('Serving Size'):
			nutrinfo += i.rstrip() + " | "
		if i.find('Total Fat'):
			nutrinfo += i + " | "
		if i.find('Protein'):
			nutrinfo += i + " | "
		if i.find('Carbs'):
			nutrinfo += i + " | "
		if i.find('Calories'):
			nutrinfo += i + " | "

	ircsock.send("PRIVMSG " + chan + " :" + nutrinfo + "\n") #putting newlines or blank lines on each append

def voteBan(hostmask, user):

	ircsock.send("PRIVMSG " + chan + " :A vote to ban " + user + " has been started. Type !vote if you wish for " 
		+ user + " to be banned. It takes 5 votes to ban. Ban will last for 1 hour.\n")

def resetVar():
	global activeVote
	activeVote = False
	global countedVotes
	countedVotes = 0

def unban(user):
	ircsock.send("UNBAN " + user) #fix this syntax, you have to unban using the hostmask NOT the user

def pollVote():
	#need to create a list of users that have already voted, so it takes 5 UNIQUE votes to ban
	#Should use hostmask checking in order to do this, not nicknames
	global activeVote
	if activeVote != False:
		global countedVotes
		countedVotes += 1
		if (countedVotes > 4):
			ircsock.send("PRIVMSG " + chan + " :" + userToKick + " will be banned for 1 hour\n")
			ircsock.send("KICK " + chan + " " + userToKick + "\n")
			ircsock.send("BAN " + chan + " " + userToKick + "\n")
			resetVar()
			t = Timer(5.0, unban(userToKick)) # this will cause problems without a list to keep track of banned users
			t.start() #unban user after 1 hour
		else:
			ircsock.send("PRIVMSG " + chan + " :Vote counted. There are currently " + str(countedVotes) 
				+ " out of 5 votes needed to ban " + userToKick + "\n")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
ircsock = ssl.wrap_socket(s)
ircsock.send("USER " + nick + " " + nick + " " + nick + " :BPBot\n")
ircsock.send("NICK " + nick + "\n")

joinChan(chan)

while 1:
	line = ircsock.recv(500)
	line.strip('\r\n')
	print line

	if line.find("PING :") != -1: #respond to Ping requests
		ping()

	if line.find("PRIVMSG " + nick + " :logoff") != -1: #logoff and close socket connection when given the kill command
		logoff()

	if line.find(":!info") != -1:
		foodItem = re.split(':!info ', line)
		findNutritionalInfo(foodItem[1].strip('\r\n'))

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

	if re.search(".+:!vote(?!ban)", line) is not None and activeVote != True: #not sure if this works
		ircsock.send("PRIVMSG " + chan + " :There is no active voting currently. To initiate a vote to ban, type !voteban nick\n")
	elif re.search(".+:!vote(?!ban)", line) is not None and activeVote == True:
		pollVote()

	if line.find(":!voteban") != -1 and activeVote != True:
		try:
			user = re.split('\s', line)
			userToKick = user[4]
			ircsock.send("WHOIS " + userToKick + "\n")
			if line.find(':No such nick/channel'): #wait for WHOIS response to ensure user exists in channel
				ircsock.send("PRIVMSG " + chan + " :No such user exists\n")
			else:
				countedVotes = 0;
				activeVote = True
				voteBan(user[0], user[4])
		except AttributeError:
				pass
		except IndexError:
				pass