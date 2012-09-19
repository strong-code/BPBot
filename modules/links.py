import urllib2, HTMLParser, os

os.environ['http_proxy']='' #this is needed for proxy problems

#parse the link assuming it is valid
def parseLink(pagesource):
	try:
		return 'Page Title: ' + pagesource.split('<title>')[1].split('</title>')[0].strip()
	except:
		return 'Page title not found!'

def isValidPage(url):
	try:
		#cheat our way past robots.txt that block us
		req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2"})
		page = urllib2.urlopen(req)
		pageType = page.info().gettype()
		if pageType == 'text/html':
			return parseLink(page.read(5000).lower())
		else:
			return
	except:
		#should log this as an error opening page
		return 'Error opening page'