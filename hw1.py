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
ai_win_dict = {
    "1" : "ok"
}

player = 1 #1 is human, 2 is AI...this is to swap players at the end of a given turn

#AIbins[1].append(1) #this will add the winning moves to the list, increasing it's probability

def ai_choice(x):
    ai_selection = random.choice(AIbins[x])
    return ai_selection

def human_choice(x):
    plays = [1,2,3]
    human_selection = random.choice(plays)
    return human_selection

def main_game_loop(NumOfSticks, player):
    while NumOfSticks >= 0:
        if player == 2:
            #This is the ai player loop
            if NumOfSticks == 1:
                NumOfSticks = 0
                winner = 1
                #ai_win_dict.clear()
            elif NumOfSticks == 2:
                play = 1
                winner = 2
            elif NumOfSticks == 3:
                play = 2
                winner = 2
            elif NumOfSticks == 4:
                play = 3
                winner = 2
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
                NumOfSticks = 0
                winner = 2
            elif NumOfSticks == 2:
                play = 1
                winner = 1
            elif NumOfSticks == 3:
                play = 2
                winner = 1
            elif NumOfSticks == 4:
                play = 3
                winner = 1
            else: 
                play = human_choice(NumOfSticks)
                print("Hello within Human move, Sticks: ", NumOfSticks, " Play: ", play)
                player = 2
            NumOfSticks = NumOfSticks - play
            player = 2
    return winner       

def increase_odds(dict):
    pass

def main():
    winner = main_game_loop(NumOfSticks, 1)
    print(ai_win_dict)
    if winner == 2:
        print ("Ai Won!")
        increase_odds(ai_win_dict)
    else:
        print ("Human Won!")
        ai_win_dict.clear()

main()    