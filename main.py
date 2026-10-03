#Random Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
password=""
for char in range(1,nr_letters+1):
    random_letter=random.choice(letters)
    password += random_letter
print(password)
nr_symbols = int(input(f"How many symbols would you like?\n"))
sym=""
for symbol in range(1,nr_symbols+1):
    random_symbol=random.choice(symbols)
    sym +=random_symbol
print(sym)
nr_numbers = int(input(f"How many numbers would you like?\n"))
num=("")
for number in range(1,nr_numbers+1):
    random_number=random.choice(numbers)
    num+=random_number
print(num)
print(f"Password generated={password}{sym}{num}")

#shuffling password
password1=[]
for char in range(1,nr_letters+1):
    password1.append(random.choice(letters))

for symbol in range(1,nr_symbols+1):
    password1.append(random.choice(symbols))

for number in range(1,nr_numbers+1):
    password1.append(random.choice(numbers))

random.shuffle(password1)
main_password="".join(password1)
print(main_password)
