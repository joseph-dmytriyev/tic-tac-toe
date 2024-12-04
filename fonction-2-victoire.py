# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:23:57 2024

@author: josep
"""

# Function to check if a player has won
def defined_victory(tab, gamer):
    # Checking rows
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] == gamer:  # Complete row for the player
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] == gamer:  # Complete column for the player
            return True
    # Checking diagonals
    if tab[0][0] == tab[1][1] == tab[2][2] == gamer:  # Main diagonal
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == gamer:  # Secondary diagonal
        return True
    return False  # No victory found
