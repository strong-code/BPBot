#A database module to handle all database needs

import sqlite3 as sql

lifts = ['squat', 'dl', 'bench', 'ohp', 'c&j', 'snatch']

#set up the database on start
def setUp():
	connection = sql.connect('BPBot.db')

	with connection:
		cur = connection.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS RepMax(User TEXT NOT NULL, Lift TEXT NOT NULL, Weight TEXT NOT NULL)')
		connection.commit()
		cur.close()
	return True

#Insert a 1RM lift into the database
def insert1RM(user, lift, weight):
	if lift not in lifts:
		return 'Not a valid lift! Valid lifts are squat, dl, bench, ohp, c&j, snatch'

	data = [(user, lift, weight),]
	connection = sql.connect('BPBot.db')

	with connection:
		cur = connection.cursor()
		rowExists = cur.execute('SELECT Lift FROM RepMax WHERE User = ?', [user])
		if rowExists is None:
			print '>>>LIFT DOES NOT EXISTS, INSERTING NEW ROW!'
			cur.executemany('REPLACE RepMax VALUES (?, ?, ?)', data)
			connection.commit()
			cur.close()
			return 'Successfully logged a new ' + lift + ' max of ' + weight + 'lb for ' + user
		else:
			data = [(weight, user, lift),]
			cur.executemany('UPDATE RepMax SET WEIGHT = ? WHERE USER = ? AND LIFT = ?', data)
			connection.commit()
			cur.close()
			return 'Successfully updated ' + lift + ' max of ' + weight + 'lb for ' + user

#Return the 1RM weight of a specified lift for a specified user
def return1RM(user, lift):
	if lift not in lifts:
		return 'Not a valid lift! Valid lifts are squat, dl, bench, ohp, c&j, snatch'

	connection = sql.connect('BPBot.db')
	with connection:
		cur = connection.cursor()
		for row in cur.execute('SELECT Weight FROM RepMax WHERE User = ? AND Lift = ?', (user, lift)):
			return user + ' has a 1RM ' + lift + ' of ' + str(row[0]) + 'lb'
		connection.commit()
		cur.close()
