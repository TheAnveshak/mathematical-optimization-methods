# This code encrypts a complete Sentence in form aX+b
# This codes works efficiently just don't use it for illegal purposes
# Caution!!! a!=even number and a!=b
# If in case aX+b==0(mod 26) it will show an error

input_text = input("Type your message:\n")
# Multiplicative coefficient = mult_coef
# Additive constant = add_const

mult = int(input("Type your multiplicative coefficient:\n"))
add = int(input("Type your additive constant:\n"))


def encrypt(text, mult_coef, add_const):
  encrypted_text = ""
  for char in text:
    if char.isalpha():
      if char.islower():
        shifted_unicode = (ord(char)-ord('a')) * (mult_coef) + (add_const) +ord('a')
        while shifted_unicode > ord('z'):
          shifted_unicode -= 26
        while shifted_unicode < ord('a'):
          shifted_unicode += 26
        encrypted_text += chr(shifted_unicode)
      elif char.isupper():
        shifted_unicode = (ord(char)-ord('A')) * (mult_coef) + (add_const) +ord('A')
        while shifted_unicode > ord('Z'):
          shifted_unicode -= 26
        while shifted_unicode < ord('A'):
          shifted_unicode += 26
        encrypted_text += chr(shifted_unicode)
    else:
      encrypted_text += char
  print(f"Encrypted text: {encrypted_text}")


encrypt(text=input_text, mult_coef=mult, add_const=add)
