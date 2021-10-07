from string import ascii_letters

# reading the text file and keeping only the letters and spaces
with open('asciitextfile.txt', 'r') as file:
    textfile = file.read()
allowed = set(ascii_letters + ' ')
answer = ''.join(l for l in textfile if l in allowed)

ASCII_values = [ord(character) for character in answer]
#print(ASCII_values)

sentence = "".join(map(chr,  ASCII_values)).split()
#print(sentence)

sentence = [word for word in sentence if not ord(word[-1]) % 2]
#print(sentence)

flist = [ord(ele) for sub in sentence for ele in sub]
#print(flist)

maximum = max(flist)
minimum = min(flist)
difference = maximum - minimum
print(difference)










