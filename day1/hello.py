# import const file/module to be used for constants
from ctypes import Union
import const

# import os module for system commands
import os


def Console(command):
    os.system(command)


Console("clear")

# new line variable syntax(?)
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

# proper multiline variable syntax
b = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

# string list
colors = ['red',
          'blue',
          'green']

# print string and int as str
print("The color list has ", len(colors), " elements.")

# for loop(?)
for i in range(0, len(colors)):
    print(colors[i])

# many different vars, many different values
a, b, c = 5, 3.2, "Hello"

# print these
print()
print(a)
print(b)
print(c)

# print imported constants from another file const.py
print("\nPI is: ", const.PI)
print("G is: ", const.G)
print("Square root of 3 is: ", const.SQRT_3)

# Literals

# numeric literals
_binary = 0b1010
_decimal = 100
_octal = 0o310
_hexadecimal = 0x12C

#   - float literal
_float_1 = 10.5
_float_2 = 1.5e2

#   - complex literal
_complex = 3.14j + 4

print()  # print empty line

print("Binary: " + str(_binary))
print("Decimal: " + str(_decimal))
print("Octal: " + str(_octal))
print("Hexadecimal: " + str(_hexadecimal))
print("Float 1: " + str(_float_1))
print("Float 2: " + str(_float_2))
print("Complex: " + str(_complex) + ", " +
      str(_complex.imag) + ", " + str(_complex.real))

print()  # print empty line

# string literals
print(r"\u20AC")  # raw string literal
print(u"\u20AC")  # unicode literal
print("\u20AC")  # finds proper literal (unicode in this case)

print()  # print empty line

# special literals
drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

print()

# list
fruits = ["apple", "mango", "orange"]

# tuple
numbers = (1, 2, 3)

# dictionary
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}

# set
vowels = {'a', 'e', 'i', 'o', 'u'}

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

print()  # empty line

# data types

# python numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is complex number?", isinstance(a, complex))

print()  # empty line

# python list
a = [1, 2.2, 'python']
print("a[0] =", a[0])
print("a[1] =", a[1])
print("a[2] =", a[2])

print("a =", a[:])  # : selects the whole list as range

print()  # empty line

# python tuple
t = (5, 'programmm', 1+3j)

print("t[1] =", t[1])
print("t[0:3] =", t[0:3])

print()  # empty line

# python set
a = {5, 2, 3, 1, 4}

print("a =", a)

b = {1, 1, 2, 3, 4, 5, 6, 5, 4, 2, 1, 8, 9, 9, 9}

print("b =", b)

ab_union = a.union(b)

print("Union of A & B =", ab_union)

print()  # empty line

# python dictionary
countries = {
    'GR': "Greece",
    'AL': "Albania",
    'RU': "Russia",
    'US': "United States",
    'UK': "United Kingdom"
}

for country in countries:
    print(country, ": ", countries[country], sep="")
