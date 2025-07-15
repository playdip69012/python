# Task-1
name = input("Ismongizni kiriting: ")
birth_year = int(input("Tug'ulgan yilingizni kiriting: "))
current_year = 2025
age = current_year - birth_year
print(name , "Sizning yoshingiz: ", age)

# Task-2
txt = 'LMaasleitbtui'
car_name = txt[1::2]
print(car_name)

# Task-3

txt = 'MsaatmiazD'
print(txt[::2])

# Task-4

txt = "I'am John. I am from London"
parts = txt.split("from ")
print(parts[1])

# Task-5

txt = "Python"
reverse = txt[::-1]
print(reverse)

# Task-6

vowels = "aeiouAEIOU"
text = input("Matin kiriting: ")
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Gapsiz hariflar soni", count)

# Task-7

numbers =[int(x) for x in input(" Sonni kiriting: ").split()]
max_value = max(numbers)
print("Eng katta son: ", max_value)

# Task-8

word = input("So'zni kiriting: ")
reversed_word = word[::-1]
if word == reversed_word:
    print("Bu palindrom")
else:
    print("Bu palindrom emas: ")

# Task-9

email = input("Emailni kiriting: ")
parts = email.split('@')
print(parts[1])

# Task-10

import random
import string
characters = string.ascii_letters + string.digits + "!@#$%^&*"
pasword = ''.join(random.choice(characters) for i in range(12))
print("Sizning parolingiz: ", pasword)