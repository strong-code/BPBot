import re, random

def decide(query):
	decision = re.compile('.d\s(.*)\s(or)?\s(.*)')
	r = random.randint(0,1)

	try:
		if decision.search(query).group(2) == 'or':
			if r == 0:
				return decision.search(query).group(1)
			else:
				return decision.search(query).group(1)
	except AttributeError:
		if r == 0:
			return 'Yes'
		else:
			return 'No'