def reverse(name):
    i = len(name) - 1
    while i >= 0:
        print(name[i], end = '')
        i-=1
    print()

reverse("Kalle")

