"""
Declaring variables 'a' and 'b'
"""

a = "hello"
b = "world"

print(a)
print(a, b)
print(a, b, sep = ':')
print(a, b, sep = ':', end = ';')
print("\n") #Making the code more readable in terminal

print(a, end = "\n\n")
print(b)
print("\n") #If i leave this new line print here, it will print 2 new lines
            #And if i remove it, it wont print new line at all?

print(a, end = '')
print(b)
