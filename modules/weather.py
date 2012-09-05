import urllib2, re

loc = re.compile('<title>Yahoo\!\sWeather\s-\s(.*)<\/title>')
cond = re.compile('(.*)<BR')

def currWeather(location):
    try:
        url = 'http://weather.yahooapis.com/forecastrss?p=%d' % int(location)
        xml = urllib2.urlopen(url)

        page = xml.read()
        a = loc.search(page).group(1)
        b = cond.search(page).group(1)

        return 'Current forecast for ' + a + ': ' + b
    except ValueError:
        return 'Must use an area code for weather module!'
    except:
        return 'Something went wrong... Alert my admin!'