#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led=11
GPIO.setup(led, GPIO.OUT)
import random
number = random.randint(1,100)
play = True
guess = True
while play:
    while guess:
        a = int(raw_input("Guess a whole number between 1 and 100:"))
        if a == number:
            GPIO.output(led, True)
            time.sleep(5)
            GPIO.output(led, False)
            print "You guessed it, the number was", number
            guess = False
            print "You win"
        elif a > number:
                if a - number > 15:
                    print a, "is very high"
                else:
                    print a, "is too high"
        elif a < number:
            if number - a > 15:
                print a, "is very low"
            else:
                print a, "is too low"
    ans = raw_input("Play Again? [Y/N]:")
    if ans == "N":
        play = False
    elif ans == "Y":
        guess = True
print "Game Exited"
GPIO.cleanup()
