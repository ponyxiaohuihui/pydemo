import requests

url = 'http://www.baidu.com'
data = requests.get(url).content

with open("a.html", "wb") as f:
    f.write(data)
