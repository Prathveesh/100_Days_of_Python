alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = "Yes"
while repeat == "Yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}. \n")

  def decrypt(plain_text, shift_amount):
    decypher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter) + 26
      new_position = position - shift_amount
      decypher_text += alphabet[new_position]
    print(f"The encoded text is {decypher_text}. \n")

  if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
  elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
  else:
    print("Enter Valid Input.")
  repeat = input('''If you want to continue type "Yes" else type "No" : \n\n''')
