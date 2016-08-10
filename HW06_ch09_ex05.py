#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body


def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True


def check_words(required_letters):
    count = 0
    file = open("words.txt", "r")
    list_of_words = file.readlines()
    for element in list_of_words:
        element = element.split()
        if uses_all(element[0], required_letters):
            count += 1
    print(count)

##############################################################################


def main():
    check_words("aeiou")
    check_words("aeiouy")

if __name__ == '__main__':
    main()
