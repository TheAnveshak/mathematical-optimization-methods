alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'brut' to decrypt for all shifts':\n")
text = input("Type your message:\n").lower()

if direction == "brut":
  def caesar_decrypt(ciphertext, shift):
    end_text = ""
    for letter in ciphertext:
      position = alphabet.index(letter)
      new_position = position - shift
      if new_position>25:
        while new_position>25:
          new_position-=26
      elif new_position <0:
        while new_position<0:
          new_position+=26
      end_text += alphabet[new_position]
    return end_text
  
  def brut_force(ciphertext):
    for shift in range(26):
      decrypted_text=caesar_decrypt(ciphertext, shift)
      print(f"Shift {shift} : {decrypted_text}")
  
  brut_force(ciphertext=text)

else:
  shift = int(input("Type the shift number:\n"))
  def caesar(start_text, shift_amount, cipher_direction):

      end_text = ""
      if cipher_direction == "decode":
          shift_amount *= -1
      for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position>25:
          while new_position>25:
            new_position-=26
        elif new_position <0:
          while new_position<0:
            new_position+=26
        end_text += alphabet[new_position]
      print(f"Here's the {direction}d result: {end_text}")
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)