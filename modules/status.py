from trigger_booleans import loaded as loadedModules
from ignore import ignoredUsers as ignored
from config import admins
import log

def showStatus():
	s = ''
	for admin in admins:
		s += admin + ' '
	size = log.getLogSize()
	lines = log.totalLines()
	return 'There are ' + str(len(loadedModules)) + ' modules loaded. Log file is ' + size + '. I have logged ' + str(lines) + ' lines. Current admins are: ' + s