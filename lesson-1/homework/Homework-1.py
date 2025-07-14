# Task-1

side = float(input("Kvadratni yonini yoz:"))
perimetr = 4 * side
area = side * side

print("Kvadrat perimetri", perimetr)
print("Kvadrat yuzi", area)

# Task-2

import math
diametr = float(input("Kattalik: diametrni kiriting: "))
length = math.pi * diametr

print ("Aylananing uzunligi:", length)

# Task-3

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
mean = (a+b)/2

print("O'rta arifmetik:", mean)

# Task-4

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

summa = a + b
product = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2

print("Yig'indisi:", summa)
print("Ko'paytmasi:", product)
print("a ning kvadrati:", a_kvadrat)
print("b ning kvadrati:", b_kvadrat)

# Task-5

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
c = float(input("Uchinchi son: "))

summa = a + b + c
average = (a + b + c) /3
maximum = max(a, b, c)

print("Yig'indisi:", summa)
print("O'rta arifmetik:", average)
print("Eng katta son:", maximum)