import collections
import requests

r = requests.get('https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8').json()

numbers = (r['data'])

# modulo20 of each number
for i in range(0,1000):
    numbers[i] = numbers[i] % 20

# displaying the statistics of each number
occurrences = collections.Counter(numbers)
print(occurrences)