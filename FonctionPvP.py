# Function to manage the player vs player game mode.
def PvP():
    tab = reset_board()  # Reset the board for a new game.
    board_morp(tab)  # Display the initial empty board.
    gamer1 = input("Joueur 1, choisissez votre symbole (X ou O) : ").upper()  # Player 1 chooses a symbol.
    while gamer1 not in ["X", "O"]:  # Validate the chosen symbol.
        gamer1 = input("Choix invalide. Choisissez entre X ou O : ").upper()  # Prompt again for valid input.
    gamer2 = "O" if gamer1 == "X" else "X"  # Assign the other symbol to Player 2.
    print(f"Joueur 1 est {gamer1} et Joueur 2 est {gamer2}.")  # Display player symbols.
    gamer = gamer1  # Start with Player 1.
    for _ in range(9):  # Maximum 9 turns in the game.
        board_morp(tab)  # Display the current state of the board.
        try:
            rows = int(input(f"Joueur {gamer}, entrez la rows (0, 1 ou 2) : "))  # Get row input.
            columns = int(input(f"Joueur {gamer}, entrez la ccolonne (0, 1 ou 2) : "))  # Get column input.
        except ValueError:  # Handle invalid inputs.
            print("Entrée invalide, veuillez entrer des nombres.")  # Error message for invalid input.
            continue  # Retry the same turn.
        if not condition_placement(tab, gamer, rows, columns):  # Validate and place the move.
            continue  # Retry if the move is invalid.

        if defined_victory(tab, gamer):  # Check for a win after the move.
            board_morp(tab)  # Display the final board state.
            print(f"Le joueur {gamer} gagne !")  # Announce the winner.
            return  # End the game.

        gamer = gamer2 if gamer == gamer1 else gamer1  # Switch turns between Player 1 and Player 2.
    board_morp(tab)  # Display the final board state.
    print("C'est un match nul.")  # Announce a draw.