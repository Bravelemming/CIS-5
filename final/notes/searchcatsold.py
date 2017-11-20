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
greenled = 4
GPIO.setup(greenled, GPIO.OUT)
yellowled = 14
GPIO.setup(yellowled, GPIO.OUT)
redled = 15
GPIO.setup(redled, GPIO.OUT)
# -- ---  -- -- -- --

# connect to database
conn = sqlite3.connect('rednews.db')
c = conn.cursor() # Mandatory for db

def readData(sql):
  for row in c.execute(sql):
    if c.execute("SELECT emailed FROM pony WHERE ups >= 15 AND title LIKE '%cat%';") == "no":
      print (row)

      # email to myself
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login('andthenraspi@gmail.com','ghostinthemachine')
      msg = "CATS detected"
      server.sendmail('andthenraspi@gmail.com','bravelemming@gmail.com','Hello!  CAT poost detected on reddit!  Your Raspy Pi has detected cats on the internet.  No, really.')
      server.quit()

      # light up LED
      GPIO.output(redled, 1)
      time.sleep(5)
      GPIO.output(redled, 0)
    else:
      pass
  c.execute("UPDATE pony SET emailed = 'yes' WHERE ups >= 15 AND title LIKE '%cat%';")
  conn.commit() # enforces write to database


# keep it going fo-ev-er.
while True:
  readData("SELECT title, subreddit, emailed, url,  FROM pony WHERE ups >= 15 AND title LIKE '%cat%';")
  time.sleep(30)




# Handling keyboard exit, still have to clean the Pins!
except keyboardInterrupt:
  print ("\n", "Keyboard exit.  Cleaning GPIO PINS!")
  GPIO.cleanup()
# cleanup on normal exit
GPIO.cleanup()