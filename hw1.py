"""
Author: Zackh Tucker
Assignment: HW1 -- CSC540
Date: 8.24.18

Description: Simple AI that learns how to play the game Sticks. 
Version: Python 3.6.3
"""

import random #required to play the game
import time #required to seed random generator with current exact time
from collections import Counter
random.seed(time.time()) #seeding the random generator with 0 to start

NumOfSticks = 100 #the number of sticks for each game
NumofGames = 10000 #AI will run this many times to train itself

AIbins = [[1,2,3] for i in range(0, NumOfSticks+1)] #this creates a bin, where each index is the number
                                               #of sticks left in the heap, and the contents are 
                                               #the potential moves to be chosen.

global ai_win_dict
ai_win_dict = {}

def ai_choice(x):
    """
    This function takes in the number of sticks left in the game, 
    represented by x, and produces a random play given what numbers
    are in that specific bin. 
    """
    ai_selection = random.choice(AIbins[x])
    return ai_selection


def human_choice(x):
    """
    This produces a random choice for the human player, simply 
    by making a list and using random.choice.
    """
    plays = [1,2,3]
    human_selection = random.choice(plays)
    return human_selection


def main_game_loop(NumOfSticks, player):
    """
    This function holds the main logic of the game, as well as maintains
    the dictionary that holds the moves made by the AI. It returns the winner, 
    to be used by the main function to dictate how to continue. 
    """
    player = random.choice([1, 2]) #1 is human, 2 is AI...this is to swap players
    while NumOfSticks >= 0:
        if player == 2:
            #This is the ai player loop
            if NumOfSticks == 1:
                NumOfSticks = 0
                winner = 1
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
            NumOfSticks = NumOfSticks - play
            player = 1
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
            NumOfSticks = NumOfSticks - play
            player = 2
    return winner       


def increase_odds(dict):
    """
    This function is the heart of the AI. By adding the moves made
    in a winning game to the set of potential choices, it increases 
    the likelihood that a "good" choice is made.
    """
    for x in dict:
        AIbins[x].append(dict[x])
    return AIbins


def print_bins(bin):
    """
    This function simply prints out the data. Counter is a library 
    that creates a dictionary where the values themselves are keys, 
    and the number of occurences is the value. Counter is O(n) as 
    opposed to the built in .count(x) which is O(n^2)
    """
    for i in range(1, len(bin)): 
        c = Counter(bin[i])
        print(i, " ",  c)
            
def main():
    """
    Main keeps track of how many games the AI wins in the simulation.
    """
    ai_win_total = 0
    for i in range(0, NumofGames) :
        winner = main_game_loop(NumOfSticks, 1)
        if winner == 2:
            ai_win_total += 1
            increase_odds(ai_win_dict)
        else:
            ai_win_dict.clear()
        i += 1
    print_bins(AIbins)
    print("AI win percentage: ", ((ai_win_total / NumofGames) * 100), "%")

main()    