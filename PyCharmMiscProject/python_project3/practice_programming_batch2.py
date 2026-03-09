from colorama import Fore, Style, init
init(autoreset=True)

# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num1 = (int(input(Fore.CYAN + "Enter First Number: ")))
num2 = (int(input(Fore.CYAN + "Enter Second Number: ")))

if num1 < num2:
    print(num1)
elif num2 < num1:
    print(num2)
print(" ")

# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
num1 = (int(input(Fore.YELLOW + "Enter First Number: ")))
num2 = (int(input(Fore.YELLOW + "Enter Second Number: ")))

if num1 != num2:
    print("Not Equal")
print(" ")

# Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
num1 = (int(input(Fore.CYAN + "Enter First Number: ")))
num2 = (int(input(Fore.CYAN + "Enter Second Number: ")))

difference = num1 - num2
print(difference)
print(" ")

# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
num1 = (int(input(Fore.YELLOW + "Enter First Number: ")))
num2 = (int(input(Fore.YELLOW + "Enter Second Number: ")))

quotient = num1 // num2
print(quotient)
print(" ")

# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
num1 = (int(input(Fore.CYAN + "Enter First Number: ")))
num2 = (int(input(Fore.CYAN + "Enter Second Number: ")))

remainder = num1 % num2
print(remainder)
print(" ")

# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []

for i in range(10):
    num = int(input(Fore.YELLOW + "Enter number: "))
    numbers.append(num)

result = numbers[0]

for i in range(1, 10):
    result -= numbers[i]

print(result)
print(" ")

# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_count = 0

for i in range(10):
    num = int(input(Fore.CYAN + "Enter number: "))

    if num % 2 == 0:
        even_count += 1

print(even_count)
print(" ")

# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
i = 0

while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1

print(" ")

# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
for i in range(0, 101):
    if i % 10 != 0 and i % 10 != 5:
        print(i)

print(" ")

# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input(Fore.YELLOW + "Enter First Number: "))
num2 = int(input(Fore.YELLOW + "Enter Second Number: "))

start = min(num1, num2)
end = max(num1, num2)

for i in range(start + 1, end):
    print(i)