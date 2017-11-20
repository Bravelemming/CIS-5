# Jack Daniel Kinne
# CS 5 Final Project
# This file is a ongoing, searchably defined webscrapper that works through reddit's
# Backdoor API, placing information into a database.  This database is
# searchable through written enquiries.
# used: Python, JSON, SQLITE.

from pprint import pprint
# called library for pretty outputs
import urllib.request
# making the transition easier for API's
import json
# json - javascript object notation for ease of reddit's API
import sqlite3
# sqlite3, a lightweight database manager for inputs/reads/enquiries.
import time
# standard library for time
import datetime
# standard library for time + date + unix time

# Connect or create rednews.db
conn = sqlite3.connect('rednews.db')

# Database will always attempt table creation FIRST
def tableCreate(conn):
  c = conn.cursor() # mandatory call for mouse
  c.execute("CREATE TABLE pony(id TEXT PRIMARY KEY, title TEXT, ups INT, author TEXT, createdUnix REAL, url TEXT, comments TEXT, subreddit TEXT, emailed TEXT)")

tableCreate(conn)

# CODEBLOCK: webscrapper that harvests information through reddit, information is
# displayed through Javascript notation and inputed into database rednews.db.

def callpony (conn, sub):
  request = urllib.request.Request(" https://www.reddit.com/r/" + sub + "/.json", headers={"User-Agent": "APQuery0.1 u/adreamremiss"})
  response = urllib.request.urlopen(request)
  response_text = response.read().decode()
  data = json.loads(response_text)
  c = conn.cursor() # mandatory call for db
  for post in data['data']['children']:
    id1 = post['data']['id']
    title1 = post['data']['title']
    ups1 = post['data']['ups']
    author1 = post['data']['author']
    createdUnix1 = post['data']['created']
    url1 = post['data']['url']
    comments1 = post['data']['num_comments']
    # CODEBLOCK: SQL database entries update.
    c.execute("INSERT OR IGNORE INTO pony (id, title, ups, author, createdUnix, url, comments, subreddit, emailed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
      (id1, title1, ups1, author1, createdUnix1, url1, comments1, sub, "no"))
  conn.commit() # enforces write to database

# This section passes a new argument to the function callpony, effectively
# harvesting MULTIPLE SUB REDDITS for data.  
# Each subreddit is also saved as a column in the DB (and searchable.)
while True:
  callpony(conn, "mylittlepony")
  time.sleep(4) # so reddit doesn't ban me
  callpony(conn, "news")
  time.sleep(4) # ditto
  callpony(conn, "aww")
  time.sleep(4) # no banning
  callpony(conn, "worldnews")
  time.sleep(4) # Kay thanks

