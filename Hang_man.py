# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:24:14 2020

@author: Chinanu
""" 
import random
import time

def selected_word(selected_player):
    word = ""
    if selected_player == str(1):
        word = input("Player 1, enter a word: ")
        print(chr(27) + "[2J") 
    else:
        with open("test.csv", "r") as f:
            words = f.readlines()
            while len(word) < 4:
                word = random.choice(words)
                
            
            
    return word.strip().upper()


def hang_Haaman_book_of_Esther():
    
    tries = 0
    failed_attempts = 0
    succeeded_attempts = 0
    selected_player = input("Select 1 to play with Human or any other character to play computer: ")
    word = selected_word(selected_player)
    letters = ["" for letter in range(len(word))]
    
    while True:
        try:
            Haamans_gallow(failed_attempts)                     
            
            for letter in letters:
                letter += "\u0332 "
                print(letter, end = ' ')

            if failed_attempts == 7:
                print("\nGame over\nPlayer 1 wins! The word is - ", word)
                break
                
            if succeeded_attempts == len(word):
                print("\nGame over\nPlayer 2 wins!")
                break

            typed_letter = (input('\n\nPlayer 2, Enter a letter: ')).upper()
            while len(typed_letter) > 1:
                typed_letter = (input('\nPlayer 2, you entered more than 1 letter.\nEnter a letter: ')).upper() 
                continue

            if typed_letter in letters:
                print("Letter has been entered.\n")
                continue              

            tries += 1           
            
            count = 0
            if typed_letter in word:
                for letter in word:
                    if typed_letter == letter:
                        letters[count] = typed_letter
                    count+=1
                succeeded_attempts += 1
            else:
                failed_attempts += 1           
            
            print()
        except:
            continue
    time.sleep(3)

def Haamans_gallow(failed_attempts):
    if failed_attempts == 0:
        print("___________")
        print("|     |")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|________\n")
        
    if failed_attempts == 1:
        print("___________")
        print("|     |")
        print("|     O")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|________\n")
        
    if failed_attempts == 2:
        print("___________")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|      ")
        print("|      ")
        print("|________\n")
        
    if failed_attempts == 3:
        print("___________")
        print("|     | ")
        print("|     O ")
        print("|     |/")
        print("|      ")
        print("|      ")
        print("|________\n")

    if failed_attempts == 4:
        print("___________")
        print("|     | ")
        print("|     O ")
        print("|    \|/")
        print("|      ")
        print("|      ")
        print("|________\n")

    if failed_attempts == 5:
        print("___________")
        print("|     | ")
        print("|     O ")
        print("|    \|/")
        print("|     | ")
        print("|      ")
        print("|________\n")

    if failed_attempts == 6:
        print("___________")
        print("|     | ")
        print("|     O ")
        print("|    \|/")
        print("|     | ")
        print("|    / ")
        print("|________\n")

    if failed_attempts == 7:
        print("___________")
        print("|     |")
        print("|     O")
        print("|    \|/")
        print("|     |")
        print("|    / \\")
        print("|________\n")        





#print("___________")
#print("|     |")
#print("|     O")
#print("|    \|/")
#print("|     |")
#print("|    / \\")
#print("|________")
            
        
if __name__ == "__main__":
    hang_Haaman_book_of_Esther()
