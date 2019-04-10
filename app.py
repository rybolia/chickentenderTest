import urllib.request, lxml
from bs4 import BeautifulSoup

# Declare variable and specify the url
my_url = 'https://goo.gl/C4BBGy'

page = urllib.request.urlopen(my_url)

soup = BeautifulSoup(page, "lxml")

data = []

# get name of sub
# name_box = soup.find_all('span', attrs={'class': 'title'})
for value in soup.find_all('div', attrs={'class': 'gridTileUnitB'}):
    data.append('')
    print (value.get_text('span', 'title'))
# name = name_box.text.strip()
# print (name_box)

# get the discount price
price_box = soup.find_all('div', attrs={'class': 'deal'})
# price = price_box.text
print (price)