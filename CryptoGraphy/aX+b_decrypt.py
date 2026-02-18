# This Decrypts a complete Sentence in ceaser cipher of Form X+b
# This is the main file of the program

text = input("Type your message:\n")

# Write a function to decrypt aX+b encoded cipher where a=1


def caesar_decrypt(ciphertext, shift):
  plaintext = ""
  for char in ciphertext:
    if char.isalpha():
      if char.islower():
        shifted_unicode = ord(char) - shift
        if shifted_unicode < ord('a'):
          shifted_unicode += 26
        elif shifted_unicode > ord('z'):
          shifted_unicode -= 26
        plaintext += chr(shifted_unicode).lower()
      elif char.isupper():
        shifted_unicode = ord(char) - shift
        if shifted_unicode < ord('A'):
          shifted_unicode += 26
        elif shifted_unicode > ord('Z'):
          shifted_unicode -= 26
        plaintext += chr(shifted_unicode).upper()

    else:
      plaintext += char
# I'm not printing this because i need to use the plaintext in the next function
  return plaintext


# Use brut force and run through all possibilities of b ranging from [0,25]


def brut_force(ciphertext):
  for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift} : {decrypted_text}")


brut_force(ciphertext=text)

# Print the possible plaintexts