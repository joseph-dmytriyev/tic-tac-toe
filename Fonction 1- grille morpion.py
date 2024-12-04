# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:43:09 2024

@author: josep
"""

tab = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the tic-tac-toe board
def board_morp(tab):
    n = len(tab)  # Size of the board (3)
    # Printing the top border line
    print("+" + "---+" * n)
    for i in range(3):  # Loop through the rows of the board
        print(f"| {tab[i][0]} | {tab[i][1]} | {tab[i][2]} |")  # Display each cell
        if i < 2:  # Horizontal separator lines between rows
            print("|---+---+---|")
    # Printing the bottom border line
    print("+" + "---+" * n)