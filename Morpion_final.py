import random  # Importing the random library for bot's move selection.

# Function to initialize an empty tic-tac-toe board (3x3 grid).
def reset_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to display the tic-tac-toe board in a formatted way.
def board_morp(tab):
    length_tab = len(tab)
    print("    0   1   2") 
    print("  ""+" + "---+" * length_tab)
    count = 0 
    for i in range(3): 
        print(f"{count} | {tab[i][0]} | {tab[i][1]} | {tab[i][2]} |") 
        if i < 2: 
            print("  " "|---+---+---|")
        count += 1 
    print("  ""+" + "---+" * length_tab)  

# Function to check if a player has won.
def defined_victory(tab, gamer):
    for i in range(3):  
        if tab[i][0] == tab[i][1] == tab[i][2] == gamer:  
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] == gamer:  
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == gamer:  
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == gamer: 
        return True
    return False 

# Function to validate and make a move on the board.
def condition_placement(tab, gamer, rows, columns):
    if rows not in range(3) or columns not in range(3): 
        print("Position invalide. Les valeurs doivent être entre 0 et 2.")  
        return False
    if tab[rows][columns] != " ":  
        print("Coup impossible, la case est déjà prise.") 
        return False
    tab[rows][columns] = gamer  
    return True  

# Function for bot to randomly select a free cell.
def bot(tab):
    empty_cases = [(i, j) for i in range(3) for j in range(3) if tab[i][j] == " "] 
    if empty_cases: 
        return random.choice(empty_cases) 
    return None 

# Function to manage the player vs bot game mode.
def PvE():
    tab = reset_board()
    gamer = "X" 
    for _ in range(9): 
        board_morp(tab) 
        if gamer == "X": 
            try:
                rows = int(input(f"Joueur {gamer}, entrez la ligne (0, 1 ou 2) : ")) 
                columns = int(input(f"Joueur {gamer}, entrez la columns (0, 1 ou 2) : ")) 
            except ValueError: 
                print("Entrée invalide, veuillez entrer des nombres.")  
                continue  
            if not condition_placement(tab, gamer, rows, columns): 
                continue 
        else:  
            print("Tour du bot...")  
            choice_bot = bot(tab)  
            if choice_bot:  
                rows, columns = choice_bot  
                print(f"Le bot joue en ({rows}, {columns})") 
                condition_placement(tab, gamer, rows, columns) 

        if defined_victory(tab, gamer):  
            board_morp(tab) 
            print(f"Le joueur {gamer} gagne ! C'est incroyable, la foule est en feu !!!!!!!") 
            return  

        gamer = "0" if gamer == "X" else "X" 
    board_morp(tab) 
    print("C'est un match nul.") 

# Function determine if there are still empty cells.
def empty_cells(board):
    for row in board:
        if " " in row:
            return True
    return False

# Function to manage the player vs player game mode.
def PvP():
    tab = reset_board() 
    board_morp(tab) 
    gamer1 = input("Joueur 1, choisissez votre symbole (X ou O) : ").upper()  
    while gamer1 not in ["X", "O"]:  
        gamer1 = input("Choix invalide. Choisissez entre X ou O : ").upper()
    gamer2 = "O" if gamer1 == "X" else "X" 
    print(f"Joueur 1 est {gamer1} et Joueur 2 est {gamer2}.") 
    gamer = gamer1 

    while empty_cells(tab):
        board_morp(tab) 
        try:
            rows = int(input(f"Joueur {gamer}, entrez la ligne (0, 1 ou 2) : "))  
            columns = int(input(f"Joueur {gamer}, entrez la colonne (0, 1 ou 2) : ")) 
        except ValueError: 
            print("Entrée invalide, veuillez entrer des numéros entre 0 et 2.") 
            continue  
        if not condition_placement(tab, gamer, rows, columns): 
            continue  

        if defined_victory(tab, gamer): 
            board_morp(tab)  
            print(f"Le joueur {gamer} gagne !, en même temps ça se sentait !")  
            return  

        gamer = gamer2 if gamer == gamer1 else gamer1 

    board_morp(tab)
    print("C'est un match nul.")  

# Function to display the main menu and handle user choices.
def menu():
    while True: 
        print("\nMenu Principal")  
        print("1. Joueur contre Bot (JcB)")  
        print("2. Joueur contre Joueur (JcJ)")  
        print("3. Quitter") 
        choice = input("Choisissez une option : ")  
        if choice == "1": 
            PvE()  
        elif choice == "2": 
            PvP()  
        elif choice == "3":  
            print("Au revoir et à JAMAIS !!!!")  
            break  
        else:  
            print("\nChoix invalide, veuillez réessayer.") 

# Start the program by displaying the main menu.
menu()