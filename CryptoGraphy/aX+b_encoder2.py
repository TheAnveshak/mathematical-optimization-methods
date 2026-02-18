# This code encrypts a complete Sentence in form aX+b
# This codes works efficiently just don't use it for illegal purposes
# Caution!!! a!=even number and a!=b
# If in case aX+b==0(mod 26) it will show an error

input_text = input("Type your message:\n")
a_range=(1,3,5,7,9,11,13,15,17,19,21,23,25)
mult = int(input("Type your multiplicative coefficient:\n"))
add = int(input("Type your additive constant:\n"))

#shifted_unicode = ((ord(char) - ord('a')+1) * mult_coef + add_const) % 26 + ord('a')
#encrypted_text += chr(shifted_unicode)
#(ord(char) - (ord('a') - 1)) will have value from 1 to 26
#((ord(char) - ord('a') + 1) * mult_coef + add_const) % 26 will have value from 0 to 25
#shifted_unicode +1 + ord('a') -1 will have value from 97 to 122

def encrypt(text, mult_coef, add_const):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_unicode = ((ord(char) - ord('a')) * mult_coef + add_const) % 26
                encrypted_text += chr(shifted_unicode+ ord('a'))
            elif char.isupper():
                shifted_unicode = ((ord(char) - ord('A')) * mult_coef + add_const) % 26
                encrypted_text += chr(shifted_unicode + ord('A'))
        else:
            encrypted_text += char
    print(f"Encrypted text: {encrypted_text}")

encrypt(input_text, mult, add)