import random,string

characters = " " + "%" + string.punctuation + string.digits + string.ascii_letters #(1. all punctuation marks, 2.all digits 3.a-z, A-Z)
characters = list(characters)
keys = characters.copy()

random.shuffle(keys)

plain_text = input("Enter the text you like to encrypt: ")
cipher_text = ""

#Encrypt Message
for letter in plain_text:
    index = characters.index(letter)
    cipher_text += keys[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")

#Decrypt Message

cipher_text = input("Enter the text you like to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += characters[index]

print(f"Encrypted Message: {cipher_text}")
print(f"Decrypted Message: {plain_text}")
