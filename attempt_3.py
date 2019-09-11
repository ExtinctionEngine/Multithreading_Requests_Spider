import requests

URL = "https://licai.eloancn.com/pcgway/gateway/v1/01"
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64;x64;rv:58.0) Gecko/20100101 Firefox/58.0",
    "Host": "licai.eloancn.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf8"
}

response = requests.get(URL, headers=Headers).text
print(response)