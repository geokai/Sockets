import requests


response = requests.get('https://httpbin.org/ip')
# print(response.json())
ip, _ = response.json()['origin'].split(',')
# print('Your IP is {0}'.format(response.json()['origin']))
print('Your IP is {0}'.format(ip))
