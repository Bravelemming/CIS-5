#Jack Daniel Kinne.  CIS 5.  9.26.15
#number guessing game, GPIO to LED blink.
#three colors, 100 numbers.  

import math
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
# Can change GPIO out at need. 7=  11=  13=

def main():
    print("")
    number = input("I have a number between 1 and 100!  Can you guess it?")
    guess(number)

def guess(number1):

    randomnumber = random.randrange(1,100)
    # Range set to 100.

    goodguess = False
    while goodguess is not True:
      if number1 > randomnumber:
        print("Too High.  Try again!")
        print("")


      elif number1 < randomnumber:
        print("Too low.  Try again!")
        print("")

      elif number1 == randomnumber:
        break
      number1 = eval(input ("What number will you guess?"))
    if number1 == randomnumber:
      playmore = input ("Good job!  You guessed the number.  Play again? (y/n)").lower()
      goodguess = True
      if playmore == "y":
        main()





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