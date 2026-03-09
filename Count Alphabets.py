
text = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase = 0

for ch in text:
    # Count vowels
    if ch.lower() in "aeiou":
        vowels += 1
    
    # Count consonants
    elif ch.isalpha():
        consonants += 1
    
    # Count spaces
    if ch == " ":
        spaces += 1
    
    # Count lowercase letters
    if ch.islower():
        lowercase += 1

print("\nString Statistics:")
print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)
