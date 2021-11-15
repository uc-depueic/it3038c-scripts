import requests, re
from bs4 import BeautifulSoup

r = requests.get('http://books.toscrape.com').content

##data = requests.get("https://www.walmart.com/cp/food/976759") 
soup = BeautifulSoup(r, 'html.parser')


##details = soup.findALL("h2",  {"class": "w_wCv lh-title ma0"})
details = soup.findAll(re.compile('h[1-6]'))
print(details) 

##print(soup.prettify())
