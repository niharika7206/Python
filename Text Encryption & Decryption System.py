def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input("Enter message: ")
key = int(input("Enter key: "))

enc = encrypt(msg.lower(), key)
print("Encrypted:", enc)

print("Decrypted:", decrypt(enc, key))
