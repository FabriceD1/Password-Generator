import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#print(len(letters))
#print(len(numbers))
#print(len(symbols))

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

###Order not randomized:
    ##e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for amount_letters in range(0,53):
    if nr_letters == amount_letters:
        random.seed(10)
        letter = random.sample(letters, amount_letters)
        #print(letter)

for amount_numbers in range(0,11):
    if nr_numbers == amount_numbers:
        random.seed(10)
        number = random.sample(numbers, amount_numbers)
        #print(number)

for amount_symbols in range(0,10):
    if nr_symbols == amount_symbols:
        random.seed(10)
        symbol = random.sample(symbols, amount_symbols)
        #print(symbol)

output = letter + number + symbol

password = ' '.join(output)

print(password)



###Order of characters randomized:
    ##e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for amount_letters in range(0,53):
    if nr_letters == amount_letters:
        random.seed(10)
        letter = random.sample(letters, amount_letters)
        #print(letter)

for amount_numbers in range(0,11):
    if nr_numbers == amount_numbers:
        random.seed(10)
        number = random.sample(numbers, amount_numbers)
        #print(number)

for amount_symbols in range(0,10):
    if nr_symbols == amount_symbols:
        random.seed(10)
        symbol = random.sample(symbols, amount_symbols)
        #print(symbol)

output = letter + number + symbol

length = len(output)
#print(length)

random.seed(10)
random_output = random.sample(output, length)

#print(random_output)

password = ' '.join(random_output)

print(password)