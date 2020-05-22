import requests
import json

latitud = '-33.447487'
longitud = '-70.673676'


url_head = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson'
url_tail = '&starttime=2020-05-20&endtime=2020-05-21'

url_entera = url_head + url_tail

#https://earthquake.usgs.gov/fdsnws/event/1/[METHOD[?PARAMETERS]]

response = requests.get(url_entera)
raw_content = json.loads(response.content)


print(raw_content)