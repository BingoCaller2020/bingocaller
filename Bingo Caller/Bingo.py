#Importing functions
import random
from time import sleep
import webbrowser
import os
import ctypes
import urllib.request
import requests
import platform
from datetime import datetime
from datetime import date

#Setting the date and times
now = datetime.now()
today = date.today()

#Bingo Calls
calls = ["Kelly's Eye - 1", "One little duck - 2", "Cup of tea - 3", "Knock at the door - 4", "Man alive - 5", "Half a dozen - 6", "Lucky for some - 7", "Garden gate - 8", "Brighton Line - 9", "Boris' Den - 10", "Legs eleven - 11", "One dozen - 12", "Unlucky for some - 13", "Valentine's Day - 14", "Young and keen - 15", "Never been kissed - 16", "Dancing Queens - 17", "Coming of age - 18", "Goodbye teens - 19", "One Score - 20", "Key of the door - 21", "Two little ducks - 22", "The Lord is my shepard - 23", "Two dozen - 24", "Duck and dive - 25", "Half a crown - 26", "Duck and a crutch - 27", "In a state - 28", "Rise and shine - 29", "Dirty Gertie - 30", "Get up and run - 31", "Buckle my shoe - 32", "Dirty knee - 33", "Ask for more - 34", "Jump and jive - 35", "Three dozen - 36", "More than eleven - 37", "Christmas cake - 38", "Steps - 39", "Life begins - 40", "Time for fun - 41", "Winnie the Pooh - 42", "Down on your knees - 43", "Droopy Drawers - 44", "Halfway there - 45", "Up to tricks - 46", "Four and seven - 47", "Four dozen - 48", "PC - 49", "It's a bullseye! - 50", "Tweak of the thumb - 51", "Chicken Vindaloo - 52", "Stuck in the tree - 53", "Man at the door - 54", "All the fives - 55", "Shotts bus - 56", "Heinz Varieties - 57", "Make them wait - 58", "Brighton Line - 59", "Grandma's getting frisky - 60", "Bakers bun - 61", "Tickety-Boo - 62", "Tickle me - 63", "Almost retired - 64", "Retirement age - 65", "Clickety click - 66", "Stairway to Heaven - 67", "Pick a mate - 68", "Anyway up - 69", "Three score and ten - 70", "Bang on the drum - 71", "Danny La Rue - 72", "Queen bee - 73", "Hit the floor - 74", "Strive and strive - 75", "Trombones - 76", "Two little crutches - 77", "Heaven's gate - 78", "One more time - 79", "Ghandi's breakfast - 80", "Stop and run - 81", "Straight on through - 82", "Time for tea - 83", "Give me more - 84", "Staying alive - 85", "Between the sticks - 86", "Torquay in Devon - 87", "Two fat ladies - 88", "Nearly there - 89", "Top of the shop - 90"]

#Version and build numbers
version = '8.1.3'
build = '361'

#Open .bat to kill all tasks
def exitProgram():
        os.startfile("C:\\Program Files (x86)\\Bingo Caller\\bin\\kill.bat")

#Defining the version checker
def versionChecker():
        print('Please wait...')
        sleep(0.25)
        with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/version.html') as f:
                retrievedVersion = f.read().decode('utf-8')
        print('Program initialising')
        sleep(1)
        if retrievedVersion > version:
                print('New major update is available')
                input('Press Enter to open the updater')
                os.startfile("C:\\Program Files (x86)\\Bingo Caller\\Updater.exe")
                exitProgram()
        else:
                return
        return

#Defining the task if the user wants to play again
def reRun():
        try: numberOfRounds = int(input('How many numbers would you like generated for this round: '))
        except ValueError:
                numberOfRounds = int(input('Please enter a valid number '))
        numberOfRoundsAsString = str(numberOfRounds)
#Checks if the user is happy with the amount of numbers being called in the game
        confimRounds = input('Are you sure you want to have ' + numberOfRoundsAsString + ' goes? Enter \'Y\' for yes and \'N\' for no: ')
        #Loops until valid input
        while confimRounds != 'y' and confimRounds != 'n':
                
                confimRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

        #Loops until user sure about number of rounds
        while confimRounds == 'n' or confimRounds == 'N':
                try: numberOfRounds = int(input('How many numbers would you like generated for this game? '))
                except ValueError:
                        numberOfRounds = int(input('Please enter a valid number '))
                numberOfRoundsAsString = str(numberOfRounds)
                confimRounds = input('Are you sure you want to have ' + numberOfRoundsAsString + ' goes? Enter \'Y\' for yes and \'N\' for no: ')
        while confimRounds != 'y' and confimRounds != 'n':
                confimRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

        #If happy, the loops end, and the code contines
        if confimRounds == 'y' or confimRounds == 'Y':
                print('Lets play bingo!')
                ready = input('Press Enter to get your first number, and again after every number called: ')
        #To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
        if ready >= '':
        #The game has started, and a variable is declared as a random number between 0 and 90
                        nextNumber = random.choice(calls)
        #A list is created for numbers already called to go in
                        alreadyCalled = []
        #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                        x = 0
                        actRound=numberOfRounds
        while x < numberOfRounds:
        #The number is reset if it has already been called; x stays the same
                if nextNumber in alreadyCalled:
                                nextNumber = random.choice(calls)
                                
        #If the number hasn't been called, then it is included in the list, printed, and reset.
                elif nextNumber not in alreadyCalled:
                        alreadyCalled.append(nextNumber)
                        print (nextNumber)
                        nextNumber = random.choice(calls)
                        actRound -=1
                        print('You have got ' + str(actRound) + ' goes left')
                        input("\n")
                        x +=1
        #Ends the loop when conditions met
                else:  

                        break
        numberOfGoesAsString = str(numberOfRounds)
        print ('You have reached your selected amount of ' + numberOfGoesAsString + ' goes.')
        sleep(0.5) 
def program():
        #Build updater
        versionChecker()
        with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/updates.html') as f:
                retrievedUpdateBuild = f.read().decode('utf-8')
        if retrievedUpdateBuild > build:
                #New build available
                print('There is a new build update available')
                sleep(1)
                print('You are running build ' + build + ' and the latest is build ' + retrievedUpdateBuild)
                sleep(1)
                print('The build update will include small, minor improvements')
                sleep(2)
                downloadBuild = input('Click Enter to continue with the update')
                sleep(1)
                print('Beginning file download ...')
                url = 'https://bingocallerapp.s3.eu-west-2.amazonaws.com/Main+Files/Bingo_Caller_Upgrade.exe'
                r = requests.get(url, allow_redirects=True)
                print("10%")
                sleep(0.5)
                print("20%")
                sleep(0.5)
                print("30%")
                sleep(0.5)
                print("40%")
                sleep(0.5)
                print("50%")
                sleep(0.5)
                print("60%")
                sleep(0.5)
                print("70%")
                sleep(0.5)
                print("80%")
                sleep(0.5)
                print("90%")
                sleep(0.5)
                print("100%")
                sleep(0.5)
                print("Unpacking, please wait.")
                open('C:\\Bingo Caller\\Bingo_Caller_Upgrade.exe', 'wb').write(r.content)         
                openFile = input('Press Enter to start the installation wizard')
                os.startfile("C:\\Bingo Caller\\Bingo_Caller_Upgrade")
                exitProgram()
        elif retrievedUpdateBuild == build:
                #No build available    
                print('Would you like to contact support?')
                #Support
                support = input('Enter \'Y\' for yes or \'N\' for no: ')
                if support == 'y' or support == 'Y':
                        questionEmail = input('Enter \'T\' for ticket creation or \'E\' for email: ')
                        if questionEmail == 't' or questionEmail == 'T':
                                webbrowser.open('https://bingocaller.atlassian.net/servicedesk/customer/portal/2')
                                exitProgram()
                        elif questionEmail == 'e' or questionEmail == 'E':
                                webbrowser.open('mailto:support@bingocaller.me', new=2)
                                exitProgram()
                elif support == 'n' or support == 'N': 

                        try: numberOfRounds = int(input('How many numbers would you like generated for this round: '))
                        except ValueError:
                                numberOfRounds = int(input('Please enter a valid number '))
                        numberOfRoundsAsString = str(numberOfRounds)
                #Checks if the user is happy with the amount of numbers being called in the game
                        confimRounds = input('Are you sure you want ' + numberOfRoundsAsString + ' goes? Enter \'Y\' for yes and \'N\' for no: ')
                        #Loops until valid input
                        while confimRounds != 'y' and confimRounds != 'n':
                                
                                confimRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

                        #Loops until user sure about number of rounds
                        while confimRounds == 'n' or confimRounds == 'N':
                                try: numberOfRounds = int(input('How many numbers would you like generated for this game? '))
                                except ValueError:
                                        numberOfRounds = int(input('Please enter a valid number '))
                                numberOfRoundsAsString = str(numberOfRounds)
                                confimRounds = input('Are you sure you want ' + numberOfRoundsAsString + ' goes? Enter \'Y\' for yes and \'N\' for no: ')
                        while confimRounds != 'y' and confimRounds != 'n':
                                confimRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

                        #If happy, the loops end, and the code contines
                        if confimRounds == 'y' or confimRounds == 'Y':
                                print('Lets play some bingo!')
                                ready = input('Press Enter to get your first number, and after every number called: ')
                        #To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
                        if ready >= '':
                        #The game has started, and a variable is declared as a random number between 0 and 90
                                        nextNumber = random.choice(calls)
                        #A list is created for numbers already called to go in
                                        alreadyCalled = []
                        #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                                        x = 0
                                        actRound=numberOfRounds
                        while x < numberOfRounds:
                        #The number is reset if it has already been called; x stays the same
                                if nextNumber in alreadyCalled:
                                                nextNumber = random.choice(calls)
                                                
                        #If the number hasn't been called, then it is included in the list, printed, and reset.
                                elif nextNumber not in alreadyCalled:
                                        alreadyCalled.append(nextNumber)
                                        print (nextNumber)
                                        nextNumber = random.choice(calls)
                                        actRound -=1
                                        print('You have ' + str(actRound) + ' goes left')
                                        input("\n")
                                        x +=1
                        #Ends the loop when conditions met
                                else:  

                                        break
                        numberOfGoesAsString = str(numberOfRounds)
                        print ('You have reached your selected amount of ' + numberOfGoesAsString + ' goes.')
                        sleep(0.5) 

def ending():
        #Asks if they want to play again
        again = input('Would you like to play Bingo Caller again? Enter \'Y\' for yes and \'X\' to exit: ')
        #Loops until valid input
        while again != 'y' and again != 'x':
                again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')
        #The game loops until the user declares 'x'
        while again == 'y':
                reRun()
                again = input('Would you like to play Bingo Caller again? Enter \'Y\' for yes and \'X\' to exit: ')
        while again != 'y' and again != 'x':
                again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')

        if again == 'x':
                print ('Goodbye, and thank you for playing Bingo Caller ' + version + '!')
                sleep(1.21)  
ctypes.windll.kernel32.SetConsoleTitleW("Bingo Caller " + version)
#Welcome
current_time = now.strftime("%H:%M:%S")
d4 = today.strftime("%b-%d-%Y")
print("The current time is " + current_time + " on " + d4)
print("\n")

sleep(1.75)
print('Welcome to Bingo Caller version ' + version)
sleep(1)
print('After you type a value, press Enter to submit it.')
sleep(1)
#Colour picking
print('Would you like to change the colour of this console window?')
colour = input('Enter \'Y\' for yes and \'N\' for no: ')
if colour == 'y':
        print('Do you know what colour would you like the console to change to?')
        yesColour = input('Enter \'Y\' for yes and \'N\' for no: ')
        if yesColour == 'n':
                # C# Program
                openColourSite = input("Press the 'Enter' key to view the possible colour choices")
                os.startfile("C:\\Program Files (x86)\\Bingo Caller\\bin\\C#\\Bingo Caller Colours.exe")
                exitProgram()
        elif yesColour == 'y':
                #Taking Colour
                colourPick=input('Enter the two numbers displayed on the previous program with NO spaces and click \'Enter\': ')
                sleep(1)
                print('Input accepted')
                sleep(1)
                print('Changing colour now')
                sleep(1.5)
                os.system('color ' + colourPick)
                sleep(0.5)
                program()
                ending()      
                exitProgram()
elif colour == 'n':
        program()
        ending()
        exitProgram()
else:
        print("Error. Invalid keystroke entered. Error code 0x636F6C6F7572")
        viewError = input("To view the errors on our website click \'Y\' for yes and \'N\' for no")
        if viewError == 'y' or viewError == 'Y':
                webbrowser.open('https://bingocaller.me/support/desktop-app/colour.html')
