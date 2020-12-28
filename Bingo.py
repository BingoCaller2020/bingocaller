#Importing functions
from random import randint
from time import sleep
import webbrowser
import os
import ctypes
import urllib.request
import requests
import platform
version = '7.0.1'
build = '7.0.1|0275'
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
       recipient = 'support@bingocaller.rf.gd'
       subject = 'Bingo Caller App Support'
       if questionEmail == 't':
              webbrowser.open('https://desk.zoho.eu/portal/bingocaller/en/newticket')
       elif questionEmail == 'e':
              webbrowser.open('mailto:support@bingocaller.zohodesk.eu', new=2)
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
                            ready = input('Press Enter to get your first number: ')
                     #To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
                     if ready >= '':
                     #The game has started, and a variable is declared as a random number between 0 and 90
                                   nextNumber = randint(1,90)
                     #A list is created for numbers already called to go in
                                   alreadyCalled = []
                     #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                                   x = 0
                     while x < numberOfRounds:
                     #The number is reset if it has already been called; x stays the same
                            if nextNumber in alreadyCalled:
                                          nextNumber = randint(1,90)
                                          
                     #If the number hasn't been called, then it is included in the list, printed, and reset.
                            elif nextNumber not in alreadyCalled:
                                   alreadyCalled.append(nextNumber)
                                   print (nextNumber)
                                   nextNumber = randint(1,90)
                                   input("Press Enter to view the next drawn number")
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