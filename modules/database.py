#A database module to handle all database needs

import sqlite3 as sql

def setUp():
	connection = sql.connect('BPBot.db')

	with connection:
		cur = connection.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS RepMax(User TEXT PRIMARY KEY NOT NULL, Lift TEXT NOT NULL, Weight TEXT NOT NULL)')
	connection.commit()
	connection.close()
	return True

def insert1RM(user, lift, weight):
	try:
		connection = sql.connect('BPBot.db')

		with connection:
			cur = connection.cursor()
			cur.execute('INSERT INTO RepMax(?, ?, ?)', user, lift, weight)
			#cur.execute('UPDATE RepMax SET WEIGHT = (?) WHERE USER = (?) AND WHERE LIFT = (?)', weight, user, lift)
			print '>>>'
		connection.commit()
		connection.close()
		return True

	except:
		return False

def return1RM(user, lift):
	try:
		connection = sql.connect('BPBot.db')

		with connection:
			cur = connection.cursor()
			cur.execute('SELECT Weight FROM RepMax WHERE User = (?) AND WHERE Lift = (?) LIMIT 1', user, lift)
			for row in rows:
				return str(row)
		connection.commit()
		connection.close()
		return True

	except:
		return False