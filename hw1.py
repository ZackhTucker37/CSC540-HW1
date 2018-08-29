"""
Author: Zackh Tucker
Assignment: HW1 -- CSC540
Date: 8.24.18

Description: Simple AI that learns how to play the game Sticks. 
Version: Python 3.6.3
"""

import random #required to play the game
import time #required to seed random generator with current exact time
random.seed(time.time()) #seeding the random generator with 0 to start

NumOfSticks = random.randint(10,101) #the number of sticks for each game -- this will get moved
NumofGames = 100000 #AI will run this many times to train itself

AIbins = [[1,2,3] for i in range(0, NumOfSticks+1)] #this creates a bin, where each index is the number
                                               #of sticks left in the heap, and the contents are 
                                               #the potential moves to be chosen.

global ai_win_dict
ai_win_dict = {}

player = 1 #1 is human, 2 is AI...this is to swap players at the end of a given turn

#print("Test of bins content: \nThere are", NumOfSticks, "bins, which are: \n", AIbins) #this is a test
#AIbins[1].append(1) #this will add the winning moves to the list, increasing it's probability
#choice = random.choice(AIbins[1]) #this is the random selector
#print(choice)
#print(AIbins)

def ai_choice(x):
    ai_selection = random.choice(AIbins[x])
    return ai_selection

def human_choice(x):
    plays = [1,2,3]
    human_selection = random.choice(plays)
    return human_selection

while NumOfSticks >= 0:
    if player == 2:
        #This is the ai player loop
        if NumOfSticks == 1: 
            NumofGames -= 1
            NumOfSticks = 0
            #ai_win_dict.clear()
        elif NumOfSticks == 2:
            play = 1
        elif NumOfSticks == 3:
            play = 2
        elif NumOfSticks == 4:
            play = 3
        else:
            play = ai_choice(NumOfSticks)
            ai_win_dict[NumOfSticks] = play
            print("Hello within AI move, Sticks: ", NumOfSticks, " Play: ", play)
            player = 1
        NumOfSticks = NumOfSticks - play
        player = 1
        #print(ai_win_dict)
    else: 
        #This is the human player loop
        if NumOfSticks == 1: 
            NumofGames -= 1
            NumOfSticks = 0
            ai_win_dict.clear()
        elif NumOfSticks == 2:
            play = 1
        elif NumOfSticks == 3:
            play = 2
        elif NumOfSticks == 4:
            play = 3
        else: 
            play = human_choice(NumOfSticks)
            print("Hello within Human move, Sticks: ", NumOfSticks, " Play: ", play)
            player = 2
        NumOfSticks = NumOfSticks - play
        player = 2         


print(ai_win_dict)
    