# coding: utf-8
"""
This is module docs.
"""
__author__ = u'lovexiaov'

import requests
import codecs

URL_HOST = u'http://www.zuimeitianqi.com'
PATH_MYCITY = u'/zuimei/myCity'  # flg=0
PATH_GETCITY = u'/zuimei/getCity'  # ?cityCode=2&cityName=香港

headers = {
    u'Origin': u'http://www.zuimeitianqi.com',
    u'Referer': u'http://www.zuimeitianqi.com/',
    u'Content-Type': u'application/x-www-form-urlencoded; charset=UTF-8',  # 必须设置 charset=UTF-8 否则返回的中文为乱码
    u'User-Agent': u'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


class Zuimei:
    def __init__(self, session=None):
        self.myCityURL = URL_HOST + PATH_MYCITY
        self.getCityURL = URL_HOST + PATH_GETCITY
        if session:
            self.session = session
        else:
            self.session = requests.Session()

    def myCity(self):
        response = self.session.post(self.myCityURL, data={u'flg': 0}, headers=headers)
        print(response.json())

    def getCity(self, cityCode, cityName):
        data = {
            u'cityCode': cityCode,
            u'cityName': cityName
        }

        response = self.session.post(self.getCityURL, data=data, headers=headers)
        # print(response.request.headers)
        print(response.text)


if __name__ == u'__main__':
    session = requests.Session()
    zuimei = Zuimei(session)
    zuimei.getCity(u'2', u'香港')
    session.close()
