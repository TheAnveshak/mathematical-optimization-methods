# This code deciphers a complete sentence of form Y=aX+b
# This code is correct and works completely fine for a_range and a!=b
# This code is not correct for a=even numbers and a==b
# the answer can be fount in a=a and b=b

#define a range for a 
# nos. coprime with 26 = 1,2,3,5,7,9,11,15,17,19,21,23,25
a_range = (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)

input_text=input("Enter the text to be deciphered: ")

# a = mult_coef = multiplicative coefficient
# b = add_const = additive constant

def decrypt(cipher_text,mult_coef,add_const):
  decrypted_message=""
  for char in cipher_text:
# I need a number such that when multiplied with (Y-b) will undo effect of multiplying with 'a'.
# pow(a, -1, 26) = a^-1 mod 26 
# numbers are from 0 to 25 so subtract 1 from Y and then add 1 to get X
# X = (Y-b) * pow(a, -1, 26) + 1
# no need for while loop as the range is from 1 to 26 as we had subtracted 1 to get range 0 to 25 and then took modulo with 26 to get the range 0 to 25 again and then added 1 to get the range 1 to 26 again.        
    if char.isalpha():
      shift = ord(char) - ord('a') if char.islower() else ord(char) - ord('A')                                                                 # Applying the decryption formula: X = (Y - b) * a^(-1) mod 26
      decrypted_shift = (shift - add_const) * pow(mult_coef, -1, 26) % 26
      decrypted_char = chr(decrypted_shift + ord('a') if char.islower() else decrypted_shift + ord('A'))
      decrypted_message += decrypted_char
    else:
      decrypted_message+=char
  return decrypted_message


def brute_force_decrypt(cipher_text):
  for mult_coef in a_range:
    for add_const in range(26):
      decrypted_text=decrypt(cipher_text,mult_coef,add_const)
      added_constant=(add_const-mult_coef)%26
      print(f"a={mult_coef}, b={added_constant} : {decrypted_text}")

brute_force_decrypt(input_text)


