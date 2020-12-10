#Importing functions
from random import randint
from time import sleep
import webbrowser
import os
import ctypes
import urllib.request
import requests
version = '7.0.0'
build = '7.0.0|0137'
ctypes.windll.kernel32.SetConsoleTitleW("Bingo Caller " + version)

print('Welcome to Bingo Caller version ' + version)
sleep(1)
print('After you type a value, press Enter to submit it.')
sleep(1)
#Activation
licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', encoding="utf-8").read()
if licencingFile != ('c808143d00122c50825b457b6229c5089e45f573949b35bee59e961bc542c78e'):
       print('This copy of Bingo Caller is not licenced.')
       input("Press \'Enter\' to get your licence key ")
       webbrowser.open('https://bingocaller.rf.gd/activation/')
       with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/serialcodesget.html') as f:
              retrievedLicenceKey = f.read().decode('utf-8')
       enterLicenceKey = input('Please enter your licence key here: ')
       print("Connecting to activation gateway.", end = '')
       sleep(1)
       print(".", end = '')
       sleep(1)
       print(".")
       sleep(2)
       if enterLicenceKey != (retrievedLicenceKey):
              print('Licencing unsuccessful. Please try again!')
              licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', 'w+',encoding="utf-8")
              licencingFile.writelines('11e08069e132737a2d3d200610c273fb0fec10fb269af6b1afb9114ec0124ac7')
              exit
       else:

              print('Activation successful!')
              sleep(2)
              licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', 'w+',encoding="utf-8")
              licencingFile.writelines('c808143d00122c50825b457b6229c5089e45f573949b35bee59e961bc542c78e')
              print('Please restart the program for the licencing to come into effect')
              licencingFile.close()
              sleep(1000000)
elif licencingFile == ('c808143d00122c50825b457b6229c5089e45f573949b35bee59e961bc542c78e'):  
       print('Checking for build updates')
       sleep(2)
       with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/updates.html') as f:
              retrievedUpdateBuild = f.read().decode('utf-8')
       if retrievedUpdateBuild > build:
              print('There is a new build available')
              sleep(1)
              print('The build update will include minor fixes but nothing major')
              downloadBuild = input('Click Enter to contine')
              sleep(1)
              print('Beginning file download ...')
              url = 'https://bingocallerapp.s3.eu-west-2.amazonaws.com/Main+Files/Bingo_Caller_Upgrade.exe'
              r = requests.get(url, allow_redirects=True)
              open('C:\\Bingo Caller\\Bingo_Caller_Upgrade.exe', 'wb').write(r.content)         
              openFile = input('Press Enter to start the installation wizard')
              os.startfile("C:\\Bingo Caller\\Bingo_Caller_Upgrade")
       else:  
              print('No build updates available')
              sleep(2)     
              print('Would you like to open a support ticket?')
              questionEmail = input('Enter \'T\' for ticket and \'E\' for email: ')
              recipient = 'support@bingocaller.rf.gd'
              subject = 'Bingo Caller App Support'
              if questionEmail == 't':
                     webbrowser.open('https://github.com/BingoCaller2020/bingocaller/issues/new/choose')
              elif questionEmail == 'e':
                     webbrowser.open('mailto:support@bingocaller.rf.gd', new=2)
                     sleep(1)
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
                                   nextNumber = randint(0,90)
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
                     
                     #When all numbers are called...
                     numberOfGoesAsString = str(numberOfRounds)
                     print ('You have reached your selected amount of ' + numberOfGoesAsString + ' goes.')
                     sleep(0.5)
                     print('Thank you for playing Bingo Caller')

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
                            sleep(2)