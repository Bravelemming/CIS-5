
# SQL ENQUIRY + GPIO LED DISPLAY
# THis SQL Enquiry searches for any mention of "cats" 
# across multiple sub reddits with at least 15 likes.
# It outputs title and subreddit as an automated email and 

# connect to database
conn = sqlite3.connect('rednews.db')
c = conn.cursor() # Mandatory for db

def readData(sql):
  for row in c.execute(sql):
    print row
    XXXXSEND EMAILXXXXX

# keep it going fo-ev-er.
while True:
  readData("SELECT title, subreddit FROM pony WHERE ups >= 15 AND title LIKE '%cat%';")
  if XXXX:  
    XXXstuff to doXXX
  else:
    pass
  time.sleep(30)




# Handling keyboard exit, still have to clean the Pins.
except keyboardInterrupt:
  print "\n", "Keyboard exit.  Cleaning GPIO PINS!"
  GPIO.cleanup()

GPIO.cleanup()