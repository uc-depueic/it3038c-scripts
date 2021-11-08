import requests, re
from bs4 import BeautifulSoup

r = requests.get('https://www.walmart.com/cp/food/976759').content

##data = requests.get("https://www.walmart.com/cp/food/976759") 
soup = BeautifulSoup(r, 'html.parser')

##details = soup.findALL("h2",  {"class": "w_wCv lh-title ma0"})
details = soup.findAll('div')
print(details) 

##print(soup.prettify())
