def reverse(name, lowercase):
    if lowercase == True:
        i = len(name) - 1
        while i >= 0:
            print(name[i].lower(), end = '')
            i-=1
        print()
    else:
        i = len(name) - 1
        while i >= 0:
            print(name[i], end = '')
            i-=1
        print()

reverse("KaLlE", True)