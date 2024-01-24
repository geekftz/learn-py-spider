import requests

url = 'http://127.0.0.1:5000/getInfo'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response = requests.get(url, headers=headers)
print('response', response)
print(response.text)
