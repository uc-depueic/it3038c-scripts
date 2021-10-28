import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.uefa.com/uefachampionsleague/statistics/players/").content 
soup = BeautifulSoup(data, 'html.parser')
##details = soup.find("div class", {"primary":"()"})
details = soup.findAll("Player")
print(details) 