from string_helper import is_name

valid_name = False

while valid_name == False:
    name = input("Your name?: ")

    if not is_name(name, ignore_case=True) == True:
        print("You did not give a proper name.")
    elif is_name(name, ignore_case=True) == True:
        valid_name == True
        print(f"Hello", name + '!')
        break