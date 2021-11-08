import json
import requests

r = requests.get('http://localhost:3000')
data = r.json()

mydict = {}

colors = {
     
    "widget1" : ' is blue',
    "widget2" : 'is green',
    "widget3" : 'is black',
    "widget4" : 'is blue'

}
print(colors)

