import urllib2, re

#Regular expressions we will use for finding the information we want
loc = re.compile('<city\sdata=\\"(.*)\\"\/><postal.*')
condition = re.compile('<condition\sdata=\\"(.*)\\"\/><temp_f.*')
fTemp = re.compile('<temp_f\sdata=\\"(.*)\\"\/><temp_c.*')
cTemp = re.compile('<temp_c\sdata=\\"(.*)\\"\/><humidity.*')

#lookup weather by zip code
def currWeather(location):
    url = "http://www.google.com/ig/api?weather=" + urllib2.quote(location)

    try:
        xml = urllib2.urlopen(url)
    except:
        #Should log errors...
        return 'Error retrieving current weather'

    page = xml.read()
    #Try to find everything we want, then format it and return the string
    try:
        a = loc.search(page).group(1)
        b = condition.search(page).group(1)
        c = fTemp.search(page).group(1)
        d = cTemp.search(page).group(1)
    except:
        return 'Could not find weather information. Did you spell your city correctly?'

    return 'Current forecast for %s is %s - %s farenheit (%s celcius)' % (a, b, c, d)
