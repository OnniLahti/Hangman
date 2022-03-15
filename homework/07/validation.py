def is_name(name):
    if not len(name) >= 2:
        return False
    if not name.isalpha():
        return False
    return True
