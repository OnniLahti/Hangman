def print_name():
    print("Onni")

def return_name(name):
    return name

def output(message, times):
    i = 0
    while i < times:
        print(str(message), end ='')
        i = i + 1
    print()

def largest(number1, number2, number3):
    largest_number = max(number1, number2, number3)
    print(largest_number)

print_name()
print(return_name("Onni"))
output("hello", 2)
largest(2, 4, 6)