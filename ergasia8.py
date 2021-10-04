import string
from string import ascii_letters

# reading the text file and keeping only the letters and spaces
with open('asciitextfile.txt', 'r') as file:
    textfile = file.read()
allowed = set(ascii_letters + ' ')
answer = ''.join(l for l in textfile if l in allowed)

# reversing the words in the text file
def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" "))

sentence = answer
sentence = reverseWordSentence(sentence)

# Caesar's algorithm
shift = int(input("Give key: "))
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = sentence.translate(table)
print(encrypted)
