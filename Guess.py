import random
import sys
pastGuess = []

#Initialises variables back to default state for the start of the game
def init(game):
    global attempt
    attempt = int(1)
    global randNum
    randNum = random.randint(0,25)
    global guessList
    guessList = []
    global low
    low = int(0)
    global high
    high = int(25)
    print ("I want to play a game\nGuess the number between 0 and 25")
    if game == "1":
        guess()
    elif game == "2":
        guessRange()

#Menu function
def menu ():
    menuSel = input("Choose an option:\n1. Play game\n2. Play easy mode\n3. See past guesses\n4. Quit\n")
    if menuCheck(menuSel):
        if (menuSel == "1"):
            init(menuSel)
        elif (menuSel == "2"):
            init(menuSel)    
        elif (menuSel == "3"):
            for pointer, items in enumerate(pastGuess):
                print("Guess number " + str(pointer+1)+":")
                print(items)
            menu()
        elif (menuSel == "4"):
            print("Thanks for playing")
            sys.exit
        
#Takes user guesses and checks them against the randomly generated number    
def guess():
    global attempt
    global guessList
    while (attempt < 8):
        userGuess = input("Enter guess: ")
        if checkGuess(userGuess):
            userGuess = int(userGuess)
            guessList.append(userGuess)
            if (userGuess == randNum):
                print("Congrats, that's right\nYou got it in " + str(attempt) + " guesses")
                print(guessList)
                pastGuess.append(guessList)
                tryAgain()
            elif (userGuess < randNum):
                print("Nope, that's too low")
                print("You have " + str(7-attempt) + " attempts left")
                attempt += 1                
            elif (userGuess > randNum):
                print("That's a bit high")
                print("You have " + str(7-attempt) + " attempts left")
                attempt += 1            
    print("Too bad, the number was " + str(randNum) + "\nYour guesses were:")
    print(guessList)
    pastGuess.append(guessList)
    tryAgain()

#Takes user guesses and checks them against the randomly generated number, displays shorterned range to help user guess number
def guessRange():
    global attempt
    global guessList
    global low
    global high
    while (attempt < 8):
        userGuess = input("Enter guess between " + str(low) + " and " + str(high)+ ": ")
        if checkGuessRange(userGuess):
            userGuess = int(userGuess)
            guessList.append(userGuess)
            if (userGuess == randNum):
                print("Congrats, that's right\nYou got it in " + str(attempt) + " guesses")
                print(guessList)
                pastGuess.append(guessList)
                tryAgain()
            elif (userGuess < randNum):
                print("Nope, that's too low")
                print("You have " + str(7-attempt) + " attempts left")
                attempt += 1
                low = userGuess
                
            elif (userGuess > randNum):
                print("That's a bit high")
                print("You have " + str(7-attempt) + " attempts left")
                attempt += 1    
                high = userGuess        
    print("Too bad, the number was " + str(randNum) + "\nYour guesses were:")
    print(guessList)
    pastGuess.append(guessList)
    tryAgain()

#Ask's player if they want to play again or quit the program    
def tryAgain():
        again = input("Return to menu? Y/N ")
        if(again == "Y"):
            menu()
        elif (again == "N"):
            print("Thanks for playing")

#Checks users guess to make sure it is a number
def checkGuess(check):
    if check.isdigit():
        check = int(check)
        if (check < 26):
            return True
        else:
            print("Guess is outside range")
            return False    
    else:
        print("Please enter an number")
        return False

#Checks users guess in the range reducing game
def checkGuessRange(check):
    if check.isdigit():
        check = int(check)
        if ((check > low) and (check < high)):
            return True
        else:
            print("Guess is outside range")
            return False    
    else:
        print("Please enter an number")
        return False

#Checks users menu input
def menuCheck(check):
    if check.isdigit():
        check = int(check)
        if (check < 5):
            return True
        else:
            print("That's not an option")
            return False
    else:
        print("Please enter an number")
        return False
menu()

