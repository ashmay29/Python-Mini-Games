def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction =='decode':
        shift_amount*=-1
    for _ in start_text:
        if _ in alphabet:
            pos =alphabet.index(_)
            newpos=pos+shift_amount
            end_text+=alphabet[newpos]
        else:
            end_text+= _
    print(end_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:")
text = input("Type your message:").lower()
shift = int(input("Type the shift number:")) % 26
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
