from bs4 import BeautifulSoup 
import urllib.request
import time

class Requester:
    def __init__(self):
        pass
    
    def get_addr(self, ip):
        while not self.check_result(ip):
            print('analyzing...')
            time.sleep(2)
            
        
        url = 'http://www.hao7188.com/ip/%s.html' % ip
        response = urllib.request.urlopen(url).read().decode('utf8')
        
        soup = BeautifulSoup(response, 'lxml')
        left_div = soup.find('div','so_list_left')
        addr_datas = []
        identity = '参考数据'
        for li in left_div.findAllNext('li'):
            if(len(li.contents) > 1):
                info = li.get_text().strip()
                if info.startswith(identity):
                    addr_datas.append(info[len(identity)+2:])
        return addr_datas

    def check_result(self, ip):
        url = 'http://www.hao7188.com/ip.asp?mysoip1221=%s' % ip
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        req.add_header('Host','www.hao7188.com')
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language','zh-CN,en-US;q=0.7,en;q=0.3')
        req.add_header('Cookie','Hm_lvt_c1b8ad8730292ff7134a139588bcf93b=1487950130,1488099404; CNZZDATA1260327247=139814576-1487944833-%7C1488097001; ASPSESSIONIDCSCRCDRD=FONFIJKABKKGBGAIPPHAGPKI; Hm_lpvt_c1b8ad8730292ff7134a139588bcf93b=1488099404')
        req.add_header('Upgrade-Insecure-Requests','1')
        req.add_header('Connection','keep-alive')
        

        with urllib.request.urlopen(req) as resp:
            #if redirected(302 status), the result is ready, 
            # else we need to wait for the result(analyzed by hao7188)
            return url != resp.geturl()
        

if __name__ == '__main__':
    req = Requester()
    addresses = req.get_addr('218.240.154.142')
    print(addresses)