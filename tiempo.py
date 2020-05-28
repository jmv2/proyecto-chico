import requests
import json

url = 'http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=4y6u4lm6bjpi&v=3.0'
response = requests.get(url)
contenido = json.loads(response.content)

daysDict = contenido['day']
todayResponse = daysDict.get('1')

print('temp minima: ' + todayResponse.get('tempmin'))
print('temp máxima: ' + todayResponse.get('tempmax'))