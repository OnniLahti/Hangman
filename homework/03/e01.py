#1-10
for i in range(1, 11):
    print(i, end ='')
    if i < 10:
        print(end = ',')
print()

#0-10, increments by 2
for i in range(0, 11, 2):
    print(i, end ='')
    if i < 10:
        print(end = ',')
print()

#10-0
for i in range(10, -1, -1):
    print(i, end ='')
    if i > 0:
        print(end = ',')
print()