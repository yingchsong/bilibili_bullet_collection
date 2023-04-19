import requests
import re
class Bullet:
    def __init__(self) -> None:
        pass
    def create_xml(BV_number):

        BV_number='BV1jc411H77P'
        response=requests.get('https://api.bilibili.com/x/player/pagelist?bvid='+BV_number+'&jsonp=jsonp')
        target=response.text
        a=re.search(r'cid":[0-9]+,',target)
        cid=a.group()[5:-1]
        oid_url = "https://api.bilibili.com/x/v1/dm/list.so?oid="+cid
        response=requests.get(oid_url)


        if response.status_code == 200:
            with open(BV_number+'.xml', 'wb') as f:
                f.write(response.content)
                print('File downloaded successfully.')
        else:
            print('Failed to download file.')
                
