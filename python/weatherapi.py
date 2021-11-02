import json
import requests

print('Please enter your zip code:')
zip = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=2d1522c8d08e3fbb3d9ecb24df63f402' % zip)
data = r.json()

##print(type(data['weather'][0]['description']))
print("The weather in %s is %s" % (zip, data['weather'][0]['description']))
