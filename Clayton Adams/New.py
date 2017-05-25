#!/usr/bin/env python3
# Magic 8 Ball IRC bot
# Created by Lance Brignoni
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#The random module allows a list to be shuffled through and randomly pick a variable.
import random
#The time module adds the concept of time into the program to simulate the idea of the 8 ball thinking.
import time
#These string variables are the possible results from the 8 ball's prediction.
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]

## Following function asks user question, then returns random results from responses
def answerQuery():
    #The code here asks for a string input in the python kernal. The code could have used raw_input to allow raw text instead of a string. However, this may be a older version of python.
    question = input("Ask and you shall receive: ")
    #After the input the string is displayed on the kernal.
    print("Let me dig deep into the waters of life, and find your answer")
    #the time module is used to wait for 2 seconds before the text "Hmmm" is displayed.
    time.sleep(2)
    print("Hmmm")
    #After "Hmmm" is displayed another 2 second wait is added.
    time.sleep(2)
    #The random module selects from the responses list randomly then prints it.
    print(random.choice(responses))
    # '\n' creates a new empty line. This is an old form of text formattiong for a lot of programming languages.
    print("\n")
    #The program is called here.
answerQuery()

## Following asks user if they would like to play again, and loops until user is finished
#An input asks to enter either 'Y' or 'N'.
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
#If someone inputs the string 'Y', then the program begins again. 
while secondQuestion == str("Y"):
    #The program is called here to begin the loop again.
    answerQuery()
    #After the progam ends again this asked once more.
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
    #If you decide to type 'N' then a input prompt is brought telling to type any key to exit.
else:
    #The program does not work beyond this point, because pressing any key creates a syntax error.
    print(input("Press any key to exit"))