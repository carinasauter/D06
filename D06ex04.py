# modify script from problem D06ex03 to write results to a file


def find_the_e():
    count = 0
    list_of_names = []
    file = open("roster.txt", "r")
    new_list = file.readlines()
    for line in new_list:
        line = line.split()
        if len(line) > 2:
            line = line[:-1]
            for element in line:
                if "e" in element or "E" in element:
                    count += 1
                    list_of_names.append(element)
        else:
            if "e" in line[0] or "E" in line[0]:
                count += 1
                list_of_names.append(line[0])
    name_file = open("list_of_names.txt", "w")
    name_file.write(
        "Number of first names containing the letter 'e': " + str(count))
    name_file.write("\nThe names are: \n" + str(list_of_names))

    file.close()
    name_file.close()


def main():
    find_the_e()

if __name__ == '__main__':
    main()
