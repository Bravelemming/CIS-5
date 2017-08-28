#Jack Daniel Kinne.  CIS 5.  9.26.15
#number guessing game, GPIO to LED blink.
#three colors, 100 numbers.  

import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# Can change GPIO out at need. 7=  11=  13=




#everything below here hasn't been evaluated or confirmed!  check it!

if guess == number:
    print("Yes, the number is " + str(number))
    
    while count > 0:
       GPIO.output(7,GPIO.HIGH)
   time.sleep(1)
   GPIO.output(7,GPIO.LOW)
      
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
   GPIO.output(11,GPIO.LOW)
                
        GPIO.output(13,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13,GPIO.LOW)
               
        count = count - 1

elif guess > number:
 print("Your guess is too high")
 
 while count > 0:
  
   GPIO.output(7,GPIO.HIGH)
   time.sleep(1)
   GPIO.output(7,GPIO.LOW)
   time.sleep(1)
   count = count - 1

else:
 print("Your guess is too low")
 while count > 0:
   GPIO.output(11,GPIO.HIGH)
   time.sleep(1)
   GPIO.output(11,GPIO.LOW)
   time.sleep(1)
   count = count - 1         

GPIO.cleanup()
