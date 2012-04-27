import re, urllib2, HTMLParser

def parseLink(pagesource):
	match = re.search('<title>(.*)<\/title>', pagesource, re.I | re.S) #find page title
	if match == None:
		return 'unable to parse URL'
	pageTitle = match.group(1).replace('\n', '').replace('\r', '') #strip/clean title before returning
	if pageTitle == None:
		pass
	return pageTitle


def getHTML(url):
	page = urllib2.urlopen(url) #need to add a timeout for this, becuase it can hang or get looped
	pageType = page.info().gettype()
	if (pageType == 'text/html'): #only return a valid mime type
		return parseLink(page.read(5000))
	else:
		pass
