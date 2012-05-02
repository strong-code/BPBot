import re, urllib2

_API_KEY_ = '7dffc948b8ce17eab6e88118e6c6e144'
_URL_ = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%s'

def getCurrentTrack(user):
	try:
		url = _URL_ %(user, _API_KEY_)
	except urllib2.HTTPerror:
		return urllib2.HTTPerror

	xml = urllib2.urlopen(url).read()

	artist = re.search('<artist.+\">(.+)<\/artist>', xml).group(1)
	track = re.search('<name>(.+)<\/name>', xml).group(1)

	return 'Currently listening to \'' + track.strip('\r\n') + '\' by ' + artist.strip('\r\n')