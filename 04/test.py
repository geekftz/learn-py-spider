import requests

# r = requests.get('https://api.github.com/events')
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# r = requests.get('https://api.github.com/events')
#
# print(r.headers)

# r = requests.get('https://api.github.com/events', stream=True)

# def test(param1, param2=100, param3=True):
#     print(param1, param2, param3)
#
#
# test(1)  # 默认参数可以不传
# test(1, "hello", False)  # 多个默认参数时，调用顺序一致
# test(1, param3=False, param2="hello")  # 调用顺序也可以不一致

# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)

requests.get('https://github.com/', timeout=0.001)
