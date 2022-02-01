boolean_variable = True
int_variable = 5
float_variable = 5.5

#casting those variables to str
a = str(boolean_variable)
b = str(int_variable)
c = str(float_variable)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(a + b)
print()

#Declaring variables for float & int conversions
a = 5.52
b = 3
c = 2
sum = b + c
sum2 = a + b
div = b / c

int1 = int(a)
int_rounded = int(round(a))
float1 = float(b)
print(sum, type(sum))
print(sum2, type(sum2))
print(div, type(div))