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
# password=""
# for i in range(0,nr_letters):
#   password=password+random.choice(letters)
# for i in range(0,nr_symbols):
#   password=password+random.choice(symbols)
# for i in range(0,nr_numbers):
#   password=password+random.choice(numbers)
# print(password)

password1=""
for i in range(0,nr_letters):
  password1=random.choices(letters,k=nr_letters)
for i in range(0,nr_symbols):
  password1=password1+random.choices(symbols,k=nr_symbols)
for i in range(0,nr_numbers):
  password1=password1+random.choices(numbers,k=nr_numbers)
print(password1)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password1=""
password1=random.choices(letters,k=nr_letters)
password1=password1+random.choices(symbols,k=nr_symbols)
password1=password1+random.choices(numbers,k=nr_numbers)
password1=random.choices(password1,k=nr_letters+nr_numbers+nr_symbols)
password1="".join(password1)
print(password1)

