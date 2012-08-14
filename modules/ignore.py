from irc_commands import *
import re

#Will be used to hold all the users we don't want to respond to
ignoredUsers = []

#checks if a user is currently being ignored via boolean value
def isIgnored(hostmask):
	for user in ignoredUsers:
		if re.match('.*\!.*@%s' % (hostmask), user): #NEEDS TO BE FIXED, GETTING AN ERROR HERE
			return True
	return False

#add a user to the ignore list by hostmask so it can't be dodged
#with a nickname change
def ignoreUser(hostmask, user):
	if isIgnored(hostmask):
		return '%s is already ignored' % user
	else:
		ignoredUsers.append(hostmask)
		return '%s is now being ignored' % user

#remove a user from the ignore list
def removeUser(hostmask, user):
	if isIgnored(hostmask):
		ignored.remove(hostmask)
		return '%s is no longer ignored' % user
	else:
		return '%s is not currently on the ignore list' % user

#show all the currently ignored users
def showList(s):
	if len(ignoredUsers) == 0:
		return 'There are no users on the ignore list'
	else:
		list = ''
		for user in ignoredUsers:
			list += user + ' '
		return 'Current ignore list: ' + str(list)