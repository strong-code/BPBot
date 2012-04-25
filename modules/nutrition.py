import HTMLParser, re, urllib2

def findNutritionalInfo(foodItem):
	'''
	Queries against the LiveStrong database to find nutritional information
	'''
	
	query = "http://www.livestrong.com/search/?mode=standard&search="
	foodItems = re.split(" ", foodItem)
	for l in foodItems:
		query += l + "+" #append each word of foodItem to the query URL

	result = urllib2.urlopen(query).read()
	if result.find('<article'):
		info = result[result.find('<article')+1:result.find('</article>')] #grab the first returned result
	info = re.split("\w>", info)
	for i in info:
		i = re.sub('<[^<]+?>', '', i)
		i = re.sub('\s+', ' ', i)
		i = re.sub('[,;]', '', i)
		i = re.sub('</spa', '', i)
		i = i.rstrip('\t\r\n\0')
		nutrinfo = ''
		
		if i.find('Serving Size'):
			nutrinfo += i.rstrip() + " | "
		if i.find('Total Fat'):
			nutrinfo += i + " | "
		if i.find('Protein'):
			nutrinfo += i + " | "
		if i.find('Carbs'):
			nutrinfo += i + " | "
		if i.find('Calories'):
			nutrinfo += i + " | "

	return nutrinfo