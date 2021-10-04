import urllib
import re
import requests
from bs4 import BeautifulSoup

# target url
url = input("Give url:")

# making requests instance
r = requests.get(url)

# using the BeautifulSoup module
soup = BeautifulSoup(r.text, 'html.parser')

# displaying the title
for title in soup.find_all('title'):
    print("Title of the website is : " + str(title.get_text()))

# displaying images
def get_img_cnt(url):
    return len(soup.find_all('img'))
print("The images in this webpage are : " + str(get_img_cnt(url)))

# displaying closing tags
my_request = urllib.request.urlopen(url)
my_HTML = my_request.read().decode("utf8")
count = len(re.findall("</.+>", my_HTML))
print("The number of closing tags is : " + str(count))