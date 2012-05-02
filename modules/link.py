import re, urllib2, HTMLParser, os

os.environ['http_proxy']='' #fixes proxy problems when running locally


def parseLink(pagesource):
	match = re.search('<title>(.*)<\/title>', pagesource, re.I | re.S) #find page title
	if match == None:
		return 'Error parsing page title'
	pageTitle = match.group(1).replace('\n', '').replace('\r', '') #strip/clean title before returning
	if pageTitle == None:
		pass
	return 'Site: ' + pageTitle.strip('\r\n')

def getHTML(url):
	try:
		page = urllib2.urlopen(url) #need to add a timeout for this, becuase it can hang or get looped
		pageType = page.info().gettype()
		if (pageType == 'text/html'): #only return a valid mime type
			return parseLink(page.read(5000))
		else:
			size = headerInfo(url)
			return pageType + " - " + str(size) + 'kB'
	except urllib2.URLError, e:
		return 'Error parsing page title'

def headerInfo(url): #grab file size info from header so we don't waste time/bandwidth loading it
	file = urllib2.urlopen(url)
	size = file.headers.get("content-length")
	file.close()
	return str(int(size)/1024) + 'kB'