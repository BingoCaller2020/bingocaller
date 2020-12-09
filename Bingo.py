#Importing functions
import random
import time
import webbrowser
import os
import ctypes
import urllib.request
version = '6.4.1'
#Welcome Message
ctypes.windll.kernel32.SetConsoleTitleW("Bingo Caller " + version)

print('Welcome to Bingo Caller version ' + version)
time.sleep(1)
print('After you type a value, press Enter to submit it.')
#Pause
time.sleep(1)
licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', encoding="utf-8").read()
if licencingFile != ('0xUYTVJV5694JAHDBA873859HAJDBNANBNX&WNDJ"W*FCNWSNDNW78863893457039827FGFGFG52JJFPA'):
       print('This copy of Bingo Caller is not licenced.')
       input("Press \'Enter\' to get your licence key ")
       webbrowser.open('https://bingocaller.rf.gd/activation/')
       with urllib.request.urlopen('https://bingocallerapp.htmlsave.net/serialcodesget.html') as f:
              retrievedLicenceKey = f.read().decode('utf-8')
       enterLicenceKey = input('Please enter your licence key here: ')
       print("Connecting to activation gateway.", end = '')
       time.sleep(1)
       print(".", end = '')
       time.sleep(1)
       print(".")
       time.sleep(2)
       if enterLicenceKey != (retrievedLicenceKey):
              print('Licencing unsuccessful. Please try again!')
              licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', 'w+',encoding="utf-8")
              licencingFile.writelines('0xUYTVJV5694JAHDBA873859HAJDBNANBNX&WNDJ"W*FCNWSNDNW78863893457039827FGFGFG52JJFPNA')
              exit
       else:

              print('Activation successful!')
              time.sleep(2)
              licencingFile = open(r'C:\\Bingo Caller\\licencing.txt', 'w+',encoding="utf-8")
              licencingFile.writelines('0xUYTVJV5694JAHDBA873859HAJDBNANBNX&WNDJ"W*FCNWSNDNW78863893457039827FGFGFG52JJFPA')
              print('Please restart the program for the licencing to come into effect')
              licencingFile.close()
              time.sleep(1000000)

else:  
       emailSubscription = open(r'C:\\Bingo Caller\\email.txt', encoding="utf-8").read()
       if emailSubscription != ('subscribed'):
              print('Would you like to subscribe to the mailing list? ')
              mailingListInput = input('Enter \'Y\' for yes and \'N\' for no ')
              if mailingListInput == 'y':
                     emailSubscription = open(r'C:\\Bingo Caller\\email.txt', 'w+',encoding="utf-8")
                     emailSubscription.writelines('subscribed')
                     emailSubscription.close
                     webbrowser.open('http://eepurl.com/hj6TbT')
       else:
                     #Main process
                                   print('Would you like to open a support ticket?')
                                   questionEmail = input('Enter \'Y\' for yes and \'N\' for no: ')
                                   if questionEmail == 'y':
                                          webbrowser.open('https://desk.zoho.eu/portal/bingocaller/en/newticket')
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
                                                        nextNumber = random.randint(0,90)
                                          #A list is created for numbers already called to go in
                                                        alreadyCalled = []
                                          #A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
                                                        x = 0
                                          while x < numberOfRounds:
                                          #The number is reset if it has already been called; x stays the same
                                                 if nextNumber in alreadyCalled:
                                                               nextNumber = random.randint(1,90)
                                                               
                                          #If the number hasn't been called, then it is included in the list, printed, and reset.
                                                 elif nextNumber not in alreadyCalled:
                                                        alreadyCalled.append(nextNumber)
                                                        print (nextNumber)
                                                        nextNumber = random.randint(1,90)
                                                        input("Press Enter to view the next drawn number")
                                                        x +=1
                                          #Ends the loop when conditions met
                                                 else:
                                                        break
                                          
                                          #When all numbers are called...
                                          numberOfGoesAsString = str(numberOfRounds)
                                          print ('You have reached your selected amount of ' + numberOfGoesAsString + ' goes.')
                                          time.sleep(0.5)
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
                                          print ('Goodbye!')
                                          time.sleep(1)