#Importing function
import random
from time import sleep
import webbrowser
import os
import ctypes
import urllib.request
import requests
import platform
calls = ["Kelly's Eye - 1", "One little duck - 2", "Cup of tea - 3", "Knock at the door - 4", "Man alive - 5", "Half a dozen - 6", "Lucky for some - 7", "Garden gate - 8", "Brighton Line - 9", "Boris' Den - 10", "Legs eleven - 11", "One dozen - 12", "Unlucky for some - 13", "Valentine's Day - 14", "Young and keen - 15", "Never been kissed - 16", "Dancing Quees - 17", "Coming of age - 18", "Goodbye teens - 19", "One Score - 20", "Key of the door - 21", "Two little ducks - 22", "The Lord is my sheperd - 23", "Two dozen - 24", "Duck and dive - 25", "Half a crown - 26", "Duck and a crutch - 27", "In a state - 28", "Rise and shine - 29", "Dirty Gerie - 30", "Get up and run - 31", "Buckly my shoe - 32", "Dirty knee - 33", "Ask for more - 34", "Jump and jive - 35", "Three dozen - 36", "More than eleven - 37", "Christmas cake - 38", "Steps - 39", "Life begins - 40", "Time for fun - 41", "Winnie the Pooh - 42", "Down on your knees - 43", "Droopy Drawers - 44", "Halfway there - 45", "Up to tricks - 46", "Four and seven - 47", "Four dozen - 48", "PC - 49", "It's a bullseye! - 50", "Tweak of the thumb - 51", "Chicken Vindaloo - 52", "Stuck in the tree - 53", "Man at the door - 54", "All the fives - 55", "Shotts bus - 56", "Heinz Varieties - 57", "Make them wait - 58", "Brighton Line - 59", "Grandma's getting frisky - 60", "Bakers bun - 61", "Tickety-Boo - 62", "Tickle me - 63", "Almost retired - 64", "Retirement age - 65", "Clickety click - 66", "Stairway to Heaven - 67", "Pick a mate - 68", "Anyway up - 69", "Three score and ten - 70", "Bang on the drum - 71", "Danny La Rue - 72", "Queen bee - 73", "Hit the floor - 74", "Strive and strive - 75", "Trombones - 76", "Two little crutches - 77", "Heavens gate - 78", "One more time - 79", "Gandhi's breakfast - 80", "Stop and run - 81", "Straight on through - 82", "Time for tea - 83", "Give me more - 84", "Staying alive - 85", "Between the sticks - 86", "Torquay in Devon - 87", "Two fat ladies - 88", "Nearly there - 89", "Top of the shop - 90"]
version = '7.1'
build = '0001'
ctypes.windll.kernel32.SetConsoleTitleW("Bingo Caller " + version)
#Welcome
print('Welcome to Bingo Caller version ' + version)
sleep(1)
print('After you type a value, press Enter to submit it.')
sleep(1)
#Activation
write = str(platform.system()) + ' ' + str(platform.architecture()) +  ' ' + str(platform.machine()) +  ' ' + str(platform.node()) +  ' ' + str(platform.processor())
licencingFile= open('C:\\Bingo Caller\\licencing.txt', "w+")
licencingFile.write(write)
licencingFile.close()
#Build updater
print('Checking for build updates')
sleep(2)
with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/updates.html') as f:
        retrievedUpdateBuild = f.read().decode('utf-8')
if retrievedUpdateBuild > build:
        #New build available
        print('There is a new build available')
        sleep(1)
        print('You are running build ' + build + ' and the latest is build ' + retrievedUpdateBuild)
        sleep(1)
        print('The build update will include small, minor improvements and security fixes')
        sleep(2)
        downloadBuild = input('Click Enter to contine')
        sleep(1)
        print('Beginning file download ...')
        url = 'https://bingocallerapp.s3.eu-west-2.amazonaws.com/Main+Files/Bingo_Caller_Upgrade.exe'
        r = requests.get(url, allow_redirects=True)
        open('C:\\Bingo Caller\\Bingo_Caller_Upgrade.exe', 'wb').write(r.content)         
        openFile = input('Press Enter to start the installation wizard')
        os.startfile("C:\\Bingo Caller\\Bingo_Caller_Upgrade")
elif retrievedUpdateBuild < build:
        #New version available
        print('Major build is available')
        sleep(1)
        print('Please run the updater to upgrade')
        sleep(1)
        print('Would you like to run the updater?')
        update = input('Enter \'Y\' for Yes and \'N\' for No ')
        sleep(1)
        if update == 'y':
                os.startfile("C:\\Program Files (x86)\\Bingo Caller\\Updater.exe")
        elif update == 'n':
                exit
elif retrievedUpdateBuild == build:
        #No build available
        print('No build updates available')
        sleep(2)     
        print('Would you like to contact support?')
        #Support
        questionEmail = input('Enter \'T\' for ticket creation, \'E\' for email or \'N\' for nothing: ')
        if questionEmail == 't':
                webbrowser.open('https://bingocaller.atlassian.net/servicedesk/customer/portal/2')
        elif questionEmail == 'e':
                webbrowser.open('mailto:requests@bingocaller.atlassian.net', new=2)
        elif questionEmail == 'n':
                def begin():
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
                        while confimRounds == 'n':
                            try: numberOfRounds = int(input('How many numbers would you like generated for this game? '))
                            except ValueError:
                                    numberOfRounds = int(input('Please enter a valid number '))
                            numberOfRoundsAsString = str(numberOfRounds)
                            confimRounds = input('Are you sure you want ' + numberOfRoundsAsString + ' goes? Enter \'Y\' for yes and \'N\' for no: ')
                        while confimRounds != 'y' and confimRounds != 'n':
                            confimRounds = input('Invalid input. Enter \'Y\' for yes and \'N\' for no: ')

                        #If happy, the loops end, and the code contines
                        if confimRounds == 'y':
                            print('Lets play some bingo!')
                            ready = input('Press Enter to get your first number, and after every numebr called: ')
                        #To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
                        if ready >= '':
                        #The game has started, and a variable is declared as a random number between 0 and 90
                                    nextNumber = random.choice(calls)
                        #A list is created for numbers already called to go in
                                    alreadyCalled = []
                        #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                                    x = 0
                        while x < numberOfRounds:
                        #The number is reset if it has already been called; x stays the same
                            if nextNumber in alreadyCalled:
                                            nextNumber = random.choice(calls)
                                            
                        #If the number hasn't been called, then it is included in the list, printed, and reset.
                            elif nextNumber not in alreadyCalled:
                                    alreadyCalled.append(nextNumber)
                                    print (nextNumber)
                                    nextNumber = random.choice(calls)
                                    input("\n")
                                    x +=1
                        #Ends the loop when conditions met
                            else:  

                                    break
                        numberOfGoesAsString = str(numberOfRounds)
                        print ('You have reached your selected amount of ' + numberOfGoesAsString + ' goes.')
                        sleep(0.5)                   
                    #Actually runs the game
                begin()
                #Asks if they want to play again
                again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
                #Loops until valid input
                while again != 'y' and again != 'x':
                        again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')
                #The game loops until the user declares 'x'
                while again == 'y':
                        begin()
                        again = input('Would you like to play again? Enter \'Y\' for yes and \'X\' to exit: ')
                while again != 'y' and again != 'x':
                        again = input('Invalid input. Enter \'Y\' for yes and \'X\' to exit: ')

                if again == 'x':
                        print ('Goodbye and thanks for playing Bingo Caller ' + version + '!')
                        sleep(1.21)