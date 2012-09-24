import sys, random, re
from random import choice

# def markovResponse(root):
# 	chanlog = open('chanlog.txt', 'r')
# 	chain = root + ' '
# 	desiredLength = random.randint(7, 16)
# 	#regex = re.compile('.*\s'+var+'\s.*', re.I)

# 	while len(chain.split()) < desiredLength:
# 		print 'Chain is ' + chain
# 		print 'Root is ' + root
# 		holder = []
# 		for line in chanlog:
# 			if re.search('.*\s'+root+'\s.*', line):
# 				holder.append(line[line.find("said: "):][6:])
# 		list = choice(holder).split()
# 		newWord = list[list.index(root)+1]
# 		chain += newWord + ' '
# 		root = newWord
# 		#newWord = re.search(r"\b" + re.escape(root) + r"\s+(\w+)", choice(holder)).group(1)
# 	return chain

#Spit out a random line from our log when JUST our name is called
def nameCall():
	chanlog = open('chanlog.txt', 'rb')
	chanlog.seek(0,2)
	bytes = chanlog.tell()
	chanlog.seek(bytes*random.random())

	while True:
		chanlog.seek(-2, 1)
		ch = chanlog.read(1)
		if ch == '\n' :
			break
		if chanlog.tell() == 1:
			break

	line = chanlog.readline()
	if '.quote' in line:
		return nameCall()
	return line[line.find("said: "):][6:]