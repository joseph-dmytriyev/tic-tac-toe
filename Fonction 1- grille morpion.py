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
    print("    0   1   2")
    print("+" + "---+" * length_tab)
    line_number=0
    for line in range(3):  # Loop through the rows of the board
        print(f"{line_number} | {tab[line][0]} | {tab[line][1]} | {tab[line][2]} |")  # Display each cell
        if line < 2:  # Horizontal separator lines between rows
            print("  " "|---+---+---|")
        line_number+=1
    # Printing the bottom border line
    print("+" + "---+" * length_tab)