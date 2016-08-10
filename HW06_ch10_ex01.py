# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def nested_sum(list_with_numbers):
    sum = 0
    for position in list_with_numbers:
        if type(position) is list:
            sum = sum + nested_sum(position)
        elif type(position) is int or type(position) is float:
            sum = sum + position
    return sum


def main():
    pass

if __name__ == '__main__':
    main()
