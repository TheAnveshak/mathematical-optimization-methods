import numpy as np
import random
#this emcodes using a random n degree polynomial 
input_text = input("Type your message:\n")

def generate_random_polynomial():
    degree = random.randint(1, 10)  
    coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]  
    return np.poly1d(coefficients)

def encrypt(text, polynomial):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                x_value = ord(char) - ord('a') + 1
                new_value = int((polynomial(x_value)) % 26)
                encrypted_text += chr(new_value + ord('a'))
            elif char.isupper():
                x_value = ord(char) - ord('A') + 1
                new_value = int((polynomial(x_value)) % 26)
                encrypted_text += chr(new_value + ord('A'))
        else:
            encrypted_text += char
    print(f"The encrypted text is : {encrypted_text}")

polynomial = generate_random_polynomial()
print("Random Polynomial:\n", polynomial)

encrypt(input_text, polynomial)
