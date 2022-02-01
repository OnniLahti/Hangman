def age():
    min = 0
    max = 120
    message = "give age, must be between 0 and 120"
    value = -1

    while value < min or value > max:
        print(message)
        value = int(input())
    print("You gave: ", value)

age()