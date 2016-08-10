#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body


def has_no_e(word):
    if "e" in word or "E" in word:
        return False
    else:
        return True


def print_no_e(list):
    count = 0
    for element in list:
        if has_no_e(element):
            print(element)
            count += 1
    percentage = count / len(list)
    print("The percentage of words not containing an 'e' in this list is: " +
          str(percentage * 100) + "%")


##############################################################################
def main():
    print_no_e(["abc", "jabber", "does", "fun", "Eat"])
if __name__ == '__main__':
    main()
