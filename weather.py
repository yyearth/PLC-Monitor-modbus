import urllib.request
import urllib 
# import re  
import json
import gzip
import os

stat = False

def testConnected():
    return1=os.system('ping 8.8.8.8')
    if return1:
        print ('ping fail')
        stat = False
    else:
        print ('ping ok')
        stat = True

def getHtml(url):  
    try:
        html= urllib.request.urlopen(url,timeout=2).read()#.decode('utf-8') 
    # print(type(html)) 
        return  html
    except Exception as e:
        html = '404'
        return html



def getWeather(loc_hanzi):  
    try:
        ct = urllib.parse.quote(loc_hanzi) 
        sweather = getHtml('http://wthrcdn.etouch.cn/weather_mini?city=%s'%(ct))
        # sweather = getHtml('http://wthrcdn.etouch.cn/weather_mini?citykey=101010100') # request weather in beijing by city id
        sweather = gzip.decompress(sweather).decode('utf-8')
        # print(sweather)
        jweather = json.loads(sweather)
        # print(jweather['data']['wendu'])
        # print(jweather['data']['forecast'])
        return jweather
    except: 
        print('getWeather error!')

def getLocation():
    loc = getHtml('http://pv.sohu.com/cityjson').decode('gbk')
    loc = loc[19:-1]
    jloc = json.loads(loc)
    # print(jloc['cname'])
    i = jloc['cname'].find('省')
    j = jloc['cname'].find('市')
    # print('%d %d'%(i,j)) 
    # print(jloc['cname'][i+1:j])
    return jloc['cname'][i+1:j]


if __name__ == '__main__':
    testConnected()
    hanzi = getLocation()
    print(hanzi)
    json = getWeather(hanzi)
    print(json)



