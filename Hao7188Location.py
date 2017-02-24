from bs4 import BeautifulSoup 
import urllib.request

class Requester:
    def __init__(self):
        pass
    
    def get_addr(self, ip):
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
                

if __name__ == '__main__':
    req = Requester()
    addresses = req.get_addr('111.198.66.136')
    print(addresses)