import sqlite3
import time
import datetime


conn = sqlite3.connect('rednews.db')

def tableCreate(conn):
	c = conn.cursor()
	try:
    		c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
	except sqlite3.OperationalError:
		pass

def dataEntry(conn, idfordb, keyword, value):
	c = conn.cursor()
	date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%M-%d %H:%M:%S'))
	c.execute("INSERT INTO stuffToPlot (ID, unix, datestamp, keyword, value) VALUES (?, ?, ?, ?, ?)",
		(idfordb, time.time(), date, keyword, value))
	conn.commit()

tableCreate(conn)

dataEntry(conn, 4, 3, 2)


