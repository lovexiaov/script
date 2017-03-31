# coding: utf-8
import requests

URL_TRANS = r'http://fanyi.baidu.com/v2transapi'


def translate(src, from_, to):
    params = {
        u'from': from_,
        u'to': to,
        u'query': src,
        u'transtype': u'translang',
        u'simple_means_flag': u'3'
    }
    response = requests.get(URL_TRANS, params)
    try:
        return response.json()
    except Exception:
        print (response.status_code)


def getdst(data):
    if data:
        return data.get(u'trans_result').get(u'data')[0].get(u'dst')


def anti_duplicate_checking():
    """
    反查重工具方法：
    1. 先将中文翻译为英文
    2. 将英文翻译为德语
    3. 将德语翻译为中文
    :return:
    """
    src = open(r'src.txt', 'r')
    dst = open(r'dst.txt', 'w')
    for line in src.readlines():
        line = line.strip()
        if not line: continue

        eng = getdst(translate(line, u'zh', u'en'))
        de = getdst(translate(eng, u'en', u'de'))

        eng = getdst(translate(de, u'de', u'en'))
        result = getdst(translate(eng, u'en', u'zh'))
        print(result)
        dst.write(result + u'\n')

    src.close()
    dst.close()


if __name__ == '__main__':
    # anti_duplicate_checking()
    print getdst(translate(u'fail the test', u'en', u'zh'))
