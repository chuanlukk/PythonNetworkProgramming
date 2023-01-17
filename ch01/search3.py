import http.client
import json
from urllib.parse import quote_plus

base = '/search'

def geocode(address):
    # 参数设置
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Foundations of Python Network Programming example search3.py'
    headers = {b'User-Agent': user_agent}
    # 用https协议连接一台特定的主机
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply[0]['lat'], reply[0]['lon'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
