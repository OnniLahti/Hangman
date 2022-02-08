def is_name(name):
    fullstring = name
    space = " "
    error = 0
    firstname, lastname = name.split(' ')

    if not fullstring.find(space) != -1:
        error += 1

    if len(firstname) < 2:
        error += 1

    if len(lastname) < 2:
        error += 1

    if not firstname.isalpha():
        error += 1

    if not lastname.isalpha():
        error += 1

    if not firstname[0].isupper():
        error += 1

    if not lastname[0].isupper():
        error += 1

    if error == 0:
        return True