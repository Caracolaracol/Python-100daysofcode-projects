#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# lengthLetters = len(letters) - 1
# length_numbers = len(numbers) - 1
# length_symbols = len(symbols) -1 

# one_letter = letters[random.3(0, lengthLetters)]
# one_number = numbers[random.randint(0,length_numbers)]
# one_symbol = symbols[random.randint(0,length_symbols)]

# password = ""
# for n in range(1, nr_letters + nr_symbols + nr_numbers):
#     if nr_letters >= n:
#         password = password + letters[random.randint(0, lengthLetters)]
#     elif nr_symbols >= n - nr_letters:
#         password = password + symbols[random.randint(0,length_symbols)]
#     elif nr_numbers >= n - nr_symbols - nr_letters:
#         password = password + numbers[random.randint(0,length_numbers)]
    
# print(password)
        

#Eazy Level
password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P