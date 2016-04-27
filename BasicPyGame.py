#!/usr/bin/env python
# Added the shebang line above to allow the user to make it executable 
# by doing chmod +x BasicPyGame.py
import time

apples = 0
gold = 0
name = ''

def start():
    global name
    print("Hello and welcome!")
    name=raw_input("What's your name: ")
    print("Welcome, " + name + "!")
    print("The objective of this game is to collect apples.")
    print("After collecting the apples you sell them.")
    choice = raw_input("Do you want to play Y/N?")
    if choice == "Y" or "y":
          begin()
    elif choice == "N" or "n":
        print "Okay, bye..."
        exit()
    else:
        exit()
def begin():
    global apples
    global gold
    global name
    print("Let's get started!")
    pick = raw_input("Do you want to pick an apple? Y/N")
    if pick == "Y":
        time.sleep(3)
        print("Pick an apple")
        apples = str(apples+1)
        if int(apples) == 1:
            print "You currently have, " +apples+ " apple"
        else:
            print "You currently have, " +apples+ " apples"
        begin()
    elif pick == "N":
        sell = raw_input("Do you want to sell your apples? Y/N")
        if sell == "Y" or "y":
            if int(apples) < 1:
                print("Sorry, " +name+ " . You have no apples to sell.")
            elif int(apples)==1:
                print("You currently have, " +apples+ "apple.")
                print("You've sold your apple.")
                gold = apples*10
            else:
                print("You currently have, " +apples+ "apples.")
                print("You've sold your apples.")
                gold = apples*10
            apples = 0
        elif sell == "N" or "n":
            print("Okay, have fun with your apple.")
        else:
            print("Should have followed my instructions. Have fun at the beginning!")
        begin()
        
start()
