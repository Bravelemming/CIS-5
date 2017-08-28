#Jack Daniel Kinne.  CIS 5.  9.26.15
#number guessing game, GPIO to LED blink.
#three colors, 100 numbers.  
import random
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
      elif number1 < randomnumber:
        print("Too low.  Try again!")
      elif number1 == randomnumber:
        break
      number1 = eval(input ("What number will you guess?"))
    if number1 == randomnumber:
      playmore = input ("Good job!  You guessed the number.  Play again? (y/n)").lower()
      if playmore == "y":
        main()
main()
