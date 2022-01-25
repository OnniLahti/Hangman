kuukausi = int(input("Anna kuukausi: "))

päivä = int(input("Anna päivä: "))

if kuukausi == 12 and päivä == 6 or kuukausi == 5 and päivä == 1:
    print("Nyt on vappu tai itsenäisyyspäivä.")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä.")