# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:43:09 2024

@author: josep
"""
#Board creation
tab = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the tic-tac-toe board
def board_morp(tab):
    length_tab = len(tab)  # Size of the board (3)
    # Printing the top border line
    print("+" + "---+" * n)
    for rows in range(3):  # Loop through the rows of the board
        print(f"| {tab[rows][0]} | {tab[rows][1]} | {tab[rows][2]} |")  # Display each cell
        if rows < 2:  # Horizontal separator lines between rows
            print("|---+---+---|")
    # Printing the bottom border line
    print("+" + "---+" * length_tab)