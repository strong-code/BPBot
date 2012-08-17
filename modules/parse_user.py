#This is intended to hold some functions to easily parse the nick!user@hostmask format
#into more logical sections. It is in its own module because it will (probably) be used all
#over the place in the future, so best to just put it here.

import re

#return the users nickname
def getNick(user):
	nick = re.match('(.*)!(~)?.*@.*', user)
	return nick.group(1)[1:]

#return the hostmask of a user
def getHostmask(user):
	hostmask = re.match('.*!~?.*@(.*)', user)
	return hostmask.group(1)

#return the username of a user
def getUsername(user):
	username = re.match('.*!~?(.*)@.*')
	return username.group(1)
