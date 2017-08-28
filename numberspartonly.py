#Jack Daniel Kinne.  CIS 5.  9.26.15
#number guessing game, GPIO to LED blink.
#three colors, 100 numbers.  

import math
import time
import random


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
