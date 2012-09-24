from irc_commands import *
import re, parse_user

#Will be used to hold all the users we don't want to respond to
ignoredUsers = []

#checks if a user is currently being ignored via boolean value
def isIgnored(nick):
	for user in ignoredUsers:
		if user == nick:
			return True
	return False

#add a user to the ignore list by nick
def ignoreUser(nick):
	if isIgnored(nick):
		return '%s is already ignored' % nick
	else:
		ignoredUsers.append(nick)
		return '%s is now being ignored' % nick

#remove a user from the ignore list
def removeUser(nick):
	if isIgnored(nick):
		ignoredUsers.remove(nick)
		return '%s is no longer ignored' % nick
	else:
		return '%s is not currently on the ignore list' % nick

#show all the currently ignored users
def showList(s):
	if len(ignoredUsers) == 0:
		return 'There are no users on the ignore list'
	else:
		list = ''
		for user in ignoredUsers:
			list += user + ' '
		return 'Current ignore list: ' + str(list)