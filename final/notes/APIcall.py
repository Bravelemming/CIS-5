from pprint import pprint
import urllib.request
import json

request = urllib.request.Request(" https://www.reddit.com/r/mylittlepony/.json", headers={"User-Agent": "APQuery0.1 u/adreamremiss"})
response = urllib.request.urlopen(request)
response_text = response.read().decode()
data = json.loads(response_text)
for post in data['data']['children']:
  print(post['data']['title'])
  print(data['data']['children'][0]['data'].keys())
