# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:39:51 2024

@author: josep
"""

# Function for the bot's choice (random free cell)
def bot(tab):
    # List of free cells on the board
    empty_case = [(i, j) for i in range(3) for j in range(3) if tab[i][j] == " "]
    if empty_case:  # If there are available cells
        return random.choice(empty_case)  # Returns a random free cell
    return None  # Returns None if no cells are free