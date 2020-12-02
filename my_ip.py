import requests


response = requests.get('https://httpbin.org/ip')
# print(response.json())
ip = response.json()['origin'].split(',')

# print('Your IP is {0}'.format(response.json()['origin']))
# 'ip' is a list object (due to the .split() method)
print('Your IP address is {0}'.format(ip[0]))
