import re, urllib2, HTMLParser, os

os.environ['http_proxy']='' #this is needed for proxy problems

#parse the link assuming it is valid
def parseLink(pagesource):
	match = re.search('<title>(.*)<\/title>', pagesource, re.I | re.S)
	if match == None:
		return 'Unable to parse page title'
	else:
		return match.group(1)

def isValidPage(url):
	try:
		page = urllib2.urlopen(url)
		pageType = page.info().gettype()
		if pageType == 'text/html':
			return parseLink(page.read(5000))
		else:
			return False
	except urllib2.URLError:
		#should log this as an error opening page
		return 'Error opening page'