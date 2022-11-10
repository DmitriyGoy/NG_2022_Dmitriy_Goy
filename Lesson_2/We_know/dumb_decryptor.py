alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = input("Enter a message to decrypt: ") 
shift = int(input("Enter encryption shift: ")) 
decryption_text = ""

for element in message.upper():
    place = alphabet.find(element)
    new_place = place + shift
    if element in alphabet:
        decryption_text += alphabet[new_place]
    else:
        decryption_text += element

print(decryption_text)