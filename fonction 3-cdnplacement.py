# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:34:13 2024

@author: josep
"""

def condition_placement(tab, gamer, rows, columns):
    # Checking if the coordinates are valid (between 0 and 2)
    if rows not in range(3) or columns not in range(3):
        print("Position invalide. Les valeurs doivent être entre 0 et 2.")
        return False
    # Checking if the cell is already occupied
    if tab[rows][columns] != " ":
        print("Coup impossible, la case est déjà prise.")
        return False
    # Placing the player's mark in the cell
    tab[rows][columns] = gamer
    return True