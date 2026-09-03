import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters =list(characters)
key = characters.copy()
random.shuffle(key)
print(f"chars:{characters}:")
print(f"key   :{key}:")
password = input("Enter a message to encrypt:")
encrypt= ""
for letter in password:
	index = characters.index(letter)
	encrypt += key[index]

print(f"Your Decrypted message: {password}: ")
print(f"Your Encrypted message: {encrypt}:")

encrypt2 = input("Enter the encrypted message: ")
password2 =""
for l in encrypt2:
	indx = key.index(l)
	password2+= characters[indx]
print(f"Your Encrypted message: {encrypt2}:")
print(f"Your Decrypted message: {password2}: ")