import json
from difflib import get_close_matches
import time

DICT = json.load(open("data.json"))

def dict_lookup(word):
    return DICT[word]

loop = True
word = (input("Enter a word to look up its definitions: ")).lower()
try:
    definitions = dict_lookup(word)
    count = 1
    for x in definitions:
        print(f"{count}: {x}")
        count += 1
except KeyError:
    try:
        while loop == True:
            closest_word = (get_close_matches(word, list(DICT.keys()), 1))[0]
            correct = input(f"Did you mean {closest_word}? Enter Y or N: ").lower()
            if correct == "y" or correct == "yes":
                definitions = dict_lookup(closest_word)
                count = 1
                for x in definitions:
                    print(f"{count}: {x}")
                    count += 1
            elif correct == "n" or correct == "no":
                print("Okay, come back another time..")
                time.sleep(1)
                loop = False
            else:
                print("Sorry, I didn't understand.. please try again")
                time.sleep(1)

    except:
        print("Sorry, I don't recognise that word.. please check again")
