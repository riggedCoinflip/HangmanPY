import json
import random

with open (r"E:\Coinflip\Documents\Programmieren\VSCode\hangmanPY\nouns.json", encoding='utf8') as f:
    words = json.load(f)

def hangman():
    searched_word = list(random.choice(words)) #use as list to make them mutable
    masked_word = list('_' for char in searched_word)
    already_tried = []
    hp = 10
    #print(searched_word) #cheat mode for debug
    print(f"You are playing Hangman. Your Word has {len(searched_word)} letters. You start with {hp} HP")
    while True:
        user_input = input(f"{','.join(masked_word)} :").lower() #a String is a list of chars
        if len(user_input) == 1:
            if user_input.isalpha():
                if user_input not in already_tried:
                    already_tried.append(user_input)
                    found_char = 0
                    for i, char in enumerate(searched_word):
                        if user_input == char.lower():
                            masked_word[i] = searched_word[i]
                            found_char += 1

                    if found_char:
                        if searched_word == masked_word: #game won, all letters are found
                            print (f"Word was {''.join(searched_word)}")
                            print ("Congratulations, you won the game!")
                            break #break the while loop
                        else: #not needed as the break would "catch" it, but better practice
                            print (f"Your letter '{user_input}' exists {found_char} times in the searched word.")
                    else:
                        hp -= 1
                        print("Your letter '{user_input}' does not exist in the searched word.")
                        if hp == 0: #game lost
                            print("Too many wrong guesses. You lost!")
                            print(f"The searched word was: {''.join(searched_word)}")
                            break #break the while loop

                    print(f"HP: {hp}  Tried letters: {','.join(char for char in already_tried)}")
                else:
                    print ("You already tried that character.")
            else:
                print ("Your input has to be a letter.")
        else:
            print ("Your input has to contain exactly 1 character")
    another_game = input("Do you want to play another game? (Y/N)")
    if another_game.lower() in ("y", "ye", "yes"):
        hangman()
    else:
        print ("Thanks for playing!")
    
if __name__ == "__main__":
    hangman()
