# Write ten random numbers to a file

import random


def write_ten_randoms():
    file = open('file_with_random_numbers.txt', 'w')
    for i in range(1, 11):
        rand_number = random.randint(1, 100)
        file.write(str(rand_number) + " ")
    file.close()

write_ten_randoms()


def main():
    write_ten_randoms()

if __name__ == '__main__':
    main()
