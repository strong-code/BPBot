from xml.dom import minidom
import urllib2

WEATHER_FEED_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def currWeather(zip):
	#Uses the code and resources specified on YDN for Python XML parsing
	url = WEATHER_FEED_URL % zip
	dom = minidom.parse(urllib2.urlopen(url))

	ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
	condition = ycondition.getAttribute('text')
	temp = ycondition.getAttribute('temp')
	loc = dom.getElementsByTagName('title')[0].firstChild.data
	
	return loc + ': currently ' + temp + ' degrees and ' + condition
