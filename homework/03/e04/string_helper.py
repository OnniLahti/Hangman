"""
Module that contains functions related to checking if name is valid.
"""
def is_name(name, ignore_case):
    """Checks if given name is valid.
    Parameters
    ----------
    ignore_case : 'boolean'
        This decides if upper or lowercase characters matter.
    name : 'string'
        It's the string that is being validated.
    space : 'char'
        This space char is used to check that the name has firstname and a lastname.
    error : 'number'
        Keeping count on the errors if they come up, if count is higher than 0, name is not valid.
    firstname, lastname : 'strings'
        Split the original string to two strings, lastname and firstname.
    Returns
    -------
    True if name is valid and False if name is invalid.
    """
    ignore_case
    space = ' '
    error = 0
    firstname, lastname = name.split(' ')

    if not name.find(space) != -1:
        error += 1

    if len(firstname) < 2:
        error += 1

    if len(lastname) < 2:
        error += 1

    if not firstname.isalpha():
        error += 1

    if not lastname.isalpha():
        error += 1

    if ignore_case == False:
        if not firstname[0].isupper():
            error += 1

        if not lastname[0].isupper():
            error += 1

    if error == 0:
        return True