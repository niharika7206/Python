import re

password = input("Enter password: ")

length = len(password) >= 8
upper = re.search("[A-Z]", password)
lower = re.search("[a-z]", password)
digit = re.search("[0-9]", password)
special = re.search("[@#$%^&*!]", password)

score = 0

if length:
    score += 1
if upper:
    score += 1
if lower:
    score += 1
if digit:
    score += 1
if special:
    score += 1

if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")
