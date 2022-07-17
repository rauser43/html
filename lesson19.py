import requests
from bs4 import BeautifulSoup

url = 'https://pythondigest.ru/new'

response = requests.get(url)

print(response.status_code)

print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)

print(type(soup.title))
print(soup.a)
print(soup.a.string)
print(soup.a.text)
print(type(soup.a.string))
print(type(soup.a.text))
print(soup.a.get('href'))
images_tags = soup.find_all('img')

for image_tag in images_tags:
    print(image_tag)

big_body_div = soup.find('div', class_='item-container')

(big_body_div)
print(type(big_body_div))
# print(big_body_div.get('class'))

(big_body_div.contents)
print(len(big_body_div.contents))
print(big_body_div.contents[1].contents[1].contents)

print(big_body_div.prettify())
print(big_body_div.cyontents[1])
print(big_body_div.contents[1].contents[1])


for child in big_body_div.children:
   print(1)
   print(child)
#
# #