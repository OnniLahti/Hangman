luku1 = int( input("luku 1: ") )
luku2 = int( input("luku 2: ") )
operaattori = input("minkä laskutoimituksen haluat tehdä? +, -, /, *: ")

if operaattori == "+" or "-" or "/" or "*":
    if luku2 > 0:
        if operaattori == "+":
            print(luku1 + luku2)
        elif operaattori == "-":
            print(luku1 - luku2)
        elif operaattori == "/":
            print(luku1 / luku2)
        elif operaattori == "*":
            print(luku1 * luku2)
    else:
        print("Nollalla ei voi jakaa")
