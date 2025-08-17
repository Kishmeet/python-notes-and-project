import random
import string
chars = " "+string.punctuation+string.digits+string.ascii_letters
#print(chars)
chars=list(chars)
key=chars.copy()
random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")
#Encryption
plain_text=input("Enter message to be encrypted: ")
print(f"Plain text: {plain_text}")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"cipher text: {cipher_text}")
#Decryption
cipher_text=input("Enter message to be encrypted: ")
print(f"encrypted text: {cipher_text}")
cipher_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"plain text: {plain_text}")