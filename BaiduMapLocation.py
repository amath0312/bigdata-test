# -*- coding:utf8 -*-
import urllib.request
import urllib.parse
import json
import config
import hashlib

class Requester:
    def __init__(self):
        self.root_url = 'http://api.map.baidu.com'

    def get_request_url(self, queryStr, sk):
        encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
        rawStr = encodedStr + config.baidu_sk
        sn = hashlib.md5(urllib.parse.quote_plus(rawStr).encode('utf8')).hexdigest()
        req_url = self.root_url+queryStr+'&sn='+sn
        print(req_url)
        return req_url
        
    def get_location(self, lat, lng):
        queryStr = '/geocoder/v2/?coordtype=wgs84ll&location=%s&output=json&ak=%s' % (lat+','+lng, config.baidu_ak)
        data = json.loads(urllib.request.urlopen(self.get_request_url(queryStr,config.baidu_sk)).read().decode('utf8'))
        return data['result']['formatted_address']


if __name__ == '__main__':
    req = Requester()
    req.get_location('39.913328', '116.454107')