from ignore import ignoredUsers as ignored
from config import admins
import log

def showStatus():
	s = ''
	for admin in admins:
		s += admin + ' '
	size = log.getLogSize()
	lines = log.totalLines()
	return 'Log file is ' + size + '. I have logged ' + str(lines) + ' lines. Current admins are: ' + s