
def greet():
    print(1)
    print(2)
    print(3)
greet()
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}?")
greet_with_name('Agustin')
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with('Agustin', 'Santiago')
greet_with(location='Agustin', name='Santiago')
# --------------
# --------------



# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
        cipher_text = ''
        if cipher_direction == 'decode':
                shift_amount *= -1
        for n in start_text:
            index_letter = alphabet.index(n)
            new_position = index_letter + shift_amount
            if cipher_direction == 'encode':
                if new_position > 26:
                    new_position = new_position - 26
            if cipher_direction == 'decode':
                if new_position < 0:
                    new_position = new_position + 26
            cipher_text = cipher_text + alphabet[new_position]
        print(f"The {cipher_direction}d text is {cipher_text}")
caesar(text, shift, direction)
