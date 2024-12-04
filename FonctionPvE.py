def PvE():
    tab = reset_board()  # Reset the board for a new game.
    gamer = "X"  # Human player starts as "X".
    for _ in range(9):  # Maximum 9 turns in the game.
        board_morp(tab)  # Display the current state of the board.
        if gamer == "X":  # If it's the human player's turn.
            try:
                rows = int(input(f"Joueur {gamer}, entrez la ligne (0, 1 ou 2) : "))  # Get row input.
                columns = int(input(f"Joueur {gamer}, entrez la columns (0, 1 ou 2) : "))  # Get column input.
            except ValueError:  # Handle invalid inputs.
                print("Entrée invalide, veuillez entrer des nombres.")  # Error message for invalid input.
                continue  # Retry the same turn.
            if not condition_placement(tab, gamer, rows, columns):  # Validate and place the move.
                continue  # Retry if the move is invalid.
        else:  # If it's the bot's turn.
            print("Tour du bot...")  # Bot's turn message.
            choice_bot = bot(tab)  # Get the bot's choice of cell.
            if choice_bot:  # If a valid cell is found.
                rows, columns = choice_bot  # Unpack the chosen cell coordinates.
                print(f"Le bot joue en ({rows}, {columns})")  # Display the bot's move.
                condition_placement(tab, gamer, rows, columns)  # Place the bot's move.

        if defined_victory(tab, gamer):  # Check for a win after the move.
            board_morp(tab)  # Display the final board state.
            print(f"Le joueur {gamer} gagne !")  # Announce the winner.
            return  # End the game.

        gamer = "0" if gamer == "X" else "X"  # Switch turns between "X" and "O".
    board_morp(tab)  # Display the final board state.
    print("C'est un match nul.")  # Announce a draw.