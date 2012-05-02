
from xml.dom import minidom
import urllib2

_API_KEY_ = '7dffc948b8ce17eab6e88118e6c6e144'
_URL_ = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%i'

def getCurrentTrack(user):
	#FIX THE STRING FORMATTING
	url = _URL_ % user % _API_KEY_
	dom = minidom.parse(urllib2.urlopen(url))

	print dom.read()