from string import ascii_letters

# reading the text file and keeping only the letters and spaces
with open('asciitextfile.txt', 'r') as file:
    textfile = file.read()
allowed = set(ascii_letters + ' ')
answer = ''.join(l for l in textfile if l in allowed)

# convert each letter to the corresponding ASCII number
ASCII_values = [ord(character) for character in answer]

sentence = "".join(map(chr,  ASCII_values)).split()

# finding words ending in an even number
sentence = [word for word in sentence if not ord(word[-1]) % 2]

# keeping the words ending in an even number in a new list
flist = [ord(ele) for sub in sentence for ele in sub]

# finding and printing the difference of max and min
maximum = max(flist)
minimum = min(flist)
difference = maximum - minimum
print(difference)










