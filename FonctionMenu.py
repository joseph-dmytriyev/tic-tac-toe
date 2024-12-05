# Function to display the main menu and handle user choices.
def menu():
    while True:  # Loop to continuously display the menu.
        print("\nMenu Principal")  # Main menu title.
        print("1. Joueur contre Bot (JcB)")  # Option for player vs bot.
        print("2. Joueur contre Joueur (JcJ)")  # Option for player vs player.
        print("3. Quitter")  # Option to quit.
        choice = input("Choisissez une option : ")  # Get user's choice.
        if choice == "1":  # If player chooses player vs bot.
            PvE()  # Start the player vs bot game mode.
        elif choice == "2":  # If player chooses player vs player.
            PvP()  # Start the player vs player game mode.
        elif choice == "3":  # If player chooses to quit.
            print("Au revoir !")  # Farewell message.
            break  # Exit the loop and terminate the program.
        else:  # If the user enters an invalid choice.
            print("\nChoix invalide, veuillez réessayer.")  # Prompt again for a valid choice.

# Start the program by displaying the main menu.
menu()