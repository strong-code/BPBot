import urllib2, HTMLParser, os, re

os.environ['http_proxy']='' #this is needed for proxy problems
titleSearch = re.compile('<title>(.*)<\/title>', re.IGNORECASE | re.MULTILINE)

#parse the link assuming it is valid
def parseLink(pagesource):
	try:
		h = HTMLParser.HTMLParser()
		title = titleSearch.search(pagesource).group(1)
		return 'Page Title: ' + h.unescape(title).encode("utf-8")
	except:
		return 'Page title not found!'

def isValidPage(url):
	try:
		#cheat our way past robots.txt that block us
		req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2"})
		page = urllib2.urlopen(req)
		pageType = page.info().gettype()
		if pageType == 'text/html':
			return parseLink(page.read())
		else:
			return
	except:
		#should log this as an error opening page
		return 'Error opening page'