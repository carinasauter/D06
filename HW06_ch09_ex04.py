#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Ah, all alcohol fell. Hellhole!
#       2: Hallo Fellah
#       3: Locofoco ?!?
##############################################################################
# Imports

# Body


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


def find_weird_words(user_input):
    file = open("words.txt", "r")
    list_of_words = file.readlines()
    for line in list_of_words:
        line = line.split()
        if uses_only(line[0], user_input):
            print(line)
    file.close()


##############################################################################
def main():
    find_weird_words("acefhlo")

if __name__ == '__main__':
    main()
