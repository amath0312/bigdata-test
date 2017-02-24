# -*- coding:utf8 -*-
import urllib.request
import json
import config

class Requester:
    def __init__(self):
        self.root_url = 'https://way.jd.com/RTBAsia/ip_location?ip=%s&appkey=%s'

    def get_gps(self, ip):
        req_url = self.root_url %(ip, config.jcloud_key)
        data = json.loads(urllib.request.urlopen(req_url).read().decode('utf8'))
        print('from jcloud:',data)
        if str(data['code']) == '10000':
            #success
            lat = str(data['result']['location']['latitude'])
            lng = str(data['result']['location']['longitude'])
            return (lat, lng)
        else:
            return (None, None)

if __name__ == '__main__':
    req = Requester()
    ip='218.240.154.142'
    lat,lng = req.get_gps(ip)
    if lat != None:
        print(lat+', '+lng)
    else:
        print('error')
