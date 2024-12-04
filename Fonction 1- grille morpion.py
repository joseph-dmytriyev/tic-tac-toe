import random  # Importing the random library for bot's move selection.

# Function to initialize an empty tic-tac-toe board (3x3 grid).
def reset_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to display the tic-tac-toe board in a formatted way.
def board_morp(tab):
    length_tab = len(tab)  # Get the size of the board (3 for a 3x3 grid).
    print("    0   1   2")  # Print column indices.
    print("  ""+" + "---+" * length_tab)  # Print the top border.
    count = 0  # Row counter for row indices.
    for i in range(3):  # Loop through each row of the board.
        print(f"{count} | {tab[i][0]} | {tab[i][1]} | {tab[i][2]} |")  # Print the row content.
        if i < 2:  # Add a horizontal divider between rows except the last row.
            print("  " "|---+---+---|")
        count += 1  # Increment row counter.
    print("  ""+" + "---+" * length_tab)  # Print the bottom border.