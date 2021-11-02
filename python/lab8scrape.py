import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.walmart.com/cp/food/976759").content 
soup = BeautifulSoup(data, 'html.parser')
details = soup.find("h2",  {"class": "w_Cv lh-title ma0"})
##details = soup.find("Seasonal flavors")
print(details) 