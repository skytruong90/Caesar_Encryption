import string

plain_text = "david"
shift = 2
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)
print(encrypted)

