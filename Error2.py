#Error Domain
er = input(
    "Would you like to include an error domain? This domain is optional,  yes or no: "
)
if er == "yes":
    val = input(
        "Would you the program to fill the error domain using an input file? If yes type \"yes\" If you ould like to fill it out yourself, type \"No \": "
    )
    if er == "yes":
        file1 = input("Enter the name of the file along with it's extension: ")
        f = open(file1, "a")
        f.write("Hey! ")
        f.close()

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
                f = open(file1, "a")
                for line in f:
                    f.write(line)
                f.close()

    return False

test = 'sample.txt'
if check_if_string_in_file(test, 'Error'):
    print('Error domain completed')
else:
    print('Error domain not completed ')

