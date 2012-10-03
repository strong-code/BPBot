from random import choice
from time import strftime
import os

#write to our log file
def writeToLog(line):
	currTime = str(strftime("%Y-%m-%d %H:%M:%S"))
	chanlog = open('chanlog.txt', 'a+')

	chanlog.write(currTime + ' ' + line + '\n')
	chanlog.close()

def closeLog():
	chanlog.flush() #do this just in case
	chanlog.close()

#search and return the keyword(s)
#Courtesy of Blice
querylog = {}
def searchLog(query):
	chanlog = open('chanlog.txt', 'r')
	quoteBuffer = []

	for line in chanlog:
		if query in line and not '.quote' in line: #quoting quote searches is redundant
			quoteBuffer.append(line.strip('\r\n\t'))
	chanlog.close()

	if not quoteBuffer:
		return 'No matches found for \'' + query + '\''
	if not query in querylog or querylog[query] >= len(quoteBuffer):
		querylog[query] = -1

	querylog[query] += 1

	if len(quoteBuffer) > 1:
		return '[Quote %d of %d] %s' % (querylog[query]+1, len(quoteBuffer), quoteBuffer[querylog[query]])
	return quoteBuffer[0]

#Return the current size of chanlog.txt
def getLogSize():
	size = float(os.path.getsize('chanlog.txt')) / 1024
	return ('%.2f' % round(size, 2)) + 'KB'

def totalLines():
	total = 0
	chanlog = open('chanlog.txt', 'r')
	for line in chanlog:
		total += 1
	chanlog.close()
	return total