#Jack Daniel Kinne.  CIS 5.  9.26.15
#number guessing game, GPIO to LED blink.
#three colors, 100 numbers.  
import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

greenled = 4
GPIO.setup(greenled, GPIO.OUT)
yellowled = 14
GPIO.setup(yellowled, GPIO.OUT)
redled = 15
GPIO.setup(redled, GPIO.OUT)

def main():
    number = eval(input("I have a number between 1 and 100!  Can you guess it?  Try:"))
    guess(number)
def guess(number1):
    randomnumber = random.randrange(1,100)
    # Range set to 100.
    goodguess = False
    while goodguess is not True:
      if number1 > randomnumber:
        print("Too High.  Try again!")
        GPIO.output(redled, 1)
        time.sleep(2)
        GPIO.output(redled, 0)
      elif number1 < randomnumber:
        print("Too low.  Try again!")
        GPIO.output(yellowled, 1)
        time.sleep(2)
        GPIO.output(yellowled, 0)
      elif number1 == randomnumber:
        break
      number1 = eval(input ("What number will you guess?"))
    if number1 == randomnumber:
      GPIO.output(greenled, 1)
      time.sleep(3)
      GPIO.output(greenled, 0)
      playmore = input ("Good job!  You guessed the number.  Play again? (y/n)").lower()
      if playmore == "y":
            main()
main()

GPIO.cleanup()
