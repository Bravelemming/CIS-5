# SQL ENQUIRY + GPIO LED DISPLAY.  Jack Daniel Kinne.
# THis SQL Enquiry searches for any mention of "cats" 
# across multiple sub reddits with at least 15 likes.
# It outputs title and subreddit as an automated email 
# and updates the SQL DB entry emailed = "yes"

# SQL server commands
import sqlite3
# Standard time library
import time
# GPIO Control
import RPi.GPIO as GPIO
# Email
import smtplib

# Board = BCM
GPIO.setmode(GPIO.BCM)
# No warnings, thanks!
GPIO.setwarnings(False)

# -- GPIO PIN SETUP --
redled = 15
GPIO.setup(redled, GPIO.OUT)
# -- ---  -- -- -- --

# connect to database
conn = sqlite3.connect('rednews.db')
c = conn.cursor() # Mandatory for db

def readData(sql):
  for row in c.execute(sql):
    data=c.fetchall()
    if len(data) != 0:
      print (row)

      # email to myself
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login('andthenraspi@gmail.com','ghostinthemachine')
      msg = "CATS detected"
      server.sendmail('andthenraspi@gmail.com','bravelemming@gmail.com','Hello!  CAT post detected on reddit!  Your Raspy Pi has detected cats on the internet.  No, really.')
      server.quit()

      # light up LED
      GPIO.output(redled, 1)
      time.sleep(5)
      GPIO.output(redled, 0)
    else:
      pass
  c.execute("UPDATE pony SET emailed = 'yes' WHERE ups>=15 AND title LIKE '%cat%';")
  conn.commit() # enforces write to database



try: 
  while True: # keep it going fo-ev-er.
    readData("SELECT title, subreddit, emailed, url  FROM pony WHERE ups >= 15 AND title LIKE '%cat%' AND emailed ='no';")
    time.sleep(30)

except:
  GPIO.cleanup()
  raise

# cleanup on normal exit
GPIO.cleanup()