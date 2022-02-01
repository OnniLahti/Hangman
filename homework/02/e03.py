import random

a = "hello"
b = 'hello'
c = """hello world"""
d = '''hello world'''
# you can use ' inside a variable and vice versa

name = "Matti"
bmi = 25.12343

print(f'{a} {name}')
print(f'{a} {name}, your bmi is: {bmi:.2f}')

print(name[0],name[4])
print(len(name)) #len() function returns string length

#Declaring variables for the 7 different functions
i = -5
k = 5, 6, 1
l = 4.56755

print(abs(i))
print(list(k))
print(float(i))
print(type(i))
print(round(l, 2))

x = random.randint(0, 10)
print(x)
print()

#Two strings from user bool check
user_strings = input("Give string 1: ")
user_strings2 = input("Give string 2: ")

print(f'give 1: {user_strings}')
print(f'give 2: {user_strings2}')
print(user_strings == user_strings2)
print()

#Comparing id's
print(f'give 1: {user_strings}')
print(f'give 2: {user_strings2}')
print(f'value {user_strings} in memory address {id(user_strings)}')
print(f'value {user_strings2} in memory address {id(user_strings2)}')
print(user_strings is user_strings2)