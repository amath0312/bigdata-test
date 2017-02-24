#!/usr/bin/env python3
# -*- coding:utf8 -*-


import urllib.request
def Submit():
    try:
        print("Prepare post")
        data = ('UserNo=%s&ipname=%s&ServiceId=xcpx2016&act=do&ServiceId=xcpx2016' % ('107','114.250.251.195')).encode('utf-8')
        req = urllib.request.Request(
            url='http://vote.e23.cn/zhuanti/xcpx2016/vote.jsp',
            data= data,
            headers={
                'Host': 'vote.e23.cn',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
                'Accept-Encoding':'gzip,deflate',
                'Refer':'http://vote.e23.cn/zhuanti/xcpx2016/?from=timeline',
                'Cookie':'JSESSIONID=D25054F066DC9CC42FEEB51DDB621300',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Content-Type':'application/x-www-form-urlencoded',
                'Content-Length':str(len(data)),
                })
        resp = urllib.request.urlopen(req)
        
        print("Get response")
        respMsg = resp.read().decode('gb2312')

        if "投票成功" in respMsg:
            print("success")
        else:
            print('fail: '+respMsg)
    except Exception as e:
        print('submit error %s' % e)


if __name__ == '__main__':
    Submit()