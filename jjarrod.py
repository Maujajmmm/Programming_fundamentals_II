
#string, function to scramble, change letters a to b, b to c, c to d, then make a decoder that reverses everything

my_string = "Once upon a midnight dreary while I pondered weak and weary"
alphabet = "abcdefghijklmnopqrstuvwxyz"
shifted_alphabet = "bcdefghijklmnopqrstuvwxyza"

def scramble(string):
    scrambled_string = []
    for char in string[::-1]:
        scrambled_string.append(char.lower())
    return scrambled_string


def change_the_letters(scrambled_string):
    letters_changed = []
    for char in scrambled_string:
        if char in alphabet:
            letter = alphabet.find(char)
            letters_changed.append(shifted_alphabet[letter])
        else:
            letters_changed.append(" ")
    return letters_changed


def changify_message(string):
    scrambled = scramble(string)
    changed = change_the_letters(scrambled)
    final_string = ""
    for char in changed:
        final_string += char
    return final_string

secret = (changify_message(my_string))
print(str(secret))

def undo_change_letters(scrambled_string):
    letters_changed = []
    for char in str(scrambled_string):
        if char in shifted_alphabet:
            letter = shifted_alphabet.find(char)
            letters_changed.append(alphabet[letter])
        elif char == " ":
            letters_changed.append(" ")
    return letters_changed


def undo_backwards_letters(scrambled_list):
    forwards_message = ""
    for char in scrambled_list[::-1]:
        forwards_message += char
    return forwards_message


def decode(mixed_string):
    step_1 = undo_change_letters(mixed_string)
    final = undo_backwards_letters(step_1)
    return final

print(decode(secret))
