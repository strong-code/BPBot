import HTMLParser, re, urllib2

def findNutritionalInfo(foodItem):
	'''
	Uses simple regex to grab the nutritional information from HTML tags
	Queries against the LiveStrong database to find nutritional information
	'''
	
	query = 'http://www.livestrong.com/search/?mode=standard&search='
	foodItems = re.split(" ", foodItem)
	for l in foodItems:
		query += l + "+" #append each word of foodItem to the query URL

	try:
		result = urllib2.urlopen(query).read()
	except urllib2.HTTPerror:
		return 'Unable to search for ' + foodItem
	try:	
		food = re.search('<h2.+><a.+\">(.+)<\/a>', result).group(1)
		servingSize = re.search('Serving\sSize:\s<span.+\">(.+)<\/span>;', result).group(1)
		cals = re.search('Calories:\s<span.+\">(.+)<\/span>', result).group(1)
		fat = re.search('Total\sFat:\s<span.+\">(.+)<\/span>', result).group(1)
		carbs = re.search('Carbs:\s<span.+\">(.+)<\/span>', result).group(1)
		protein = re.search('Protein:\s<span.+\">(.+)<\/span>', result).group(1)

		return food + ': Serving size ' + servingSize + ' | ' + cals + ' calories | ' + fat + ' of fat | ' + carbs + ' of carbs | ' + protein + ' of protein'
	except AttributeError:
		pass