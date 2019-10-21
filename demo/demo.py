import requests
import time
import random
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

dms = []
font = "萍方.ttf"  #词云字体
#返回集数代码号(cookie会过期)
def get_collection():
    url = 'https://acs.youku.com/h5/mtop.youku.play.ups.appinfo.get/1.1/?jsv=2.4.16&appKey=24679788&t=1571556921887&sign=8738e23969b0d29b16e0783baf01271a&api=mtop.youku.play.ups.appinfo.get&v=1.1&timeout=20000&YKPid=20160317PLF000211&YKLoginRequest=true&AntiFlood=true&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22steal_params%22%3A%22%7B%5C%22ccode%5C%22%3A%5C%220502%5C%22%2C%5C%22client_ip%5C%22%3A%5C%22192.168.1.1%5C%22%2C%5C%22utid%5C%22%3A%5C%22FzbCFPXWOEYCAXF2UFa2UaQI%5C%22%2C%5C%22client_ts%5C%22%3A1571556921%2C%5C%22version%5C%22%3A%5C%221.9.8%5C%22%2C%5C%22ckey%5C%22%3A%5C%22121%23BNGlkEXOvJllVlHp%2BFSrlVbYeczE4ujVbdQ5x5T5eMCZOW16MmeulG9GAcfdK5j9lGgY%2BzpIKM9lOQrnqkDIlw9m4JkLgzjVlwgy%2BaPIKMtLA3rnEkDIll9YOc8fDuj9lGgY%2BzpIDM9lOQrJEIDhllXYAQRhu1eeLlSVD0g60jzVpSCge69GhXb0CO3LzPBhbZssk%2BHXQtK0bZibnnx9pCibC6548uBmlw%2BlErcLF9FbkZsbnnxlpZb0C6048u%2FmCbibCeIaQtK0bZibnnC9pCibCZ04kG%2FRbviO4NRaFYAVBPZoJzxANCehqyzTGmR2yPsDkNHXFHqLl%2BHXlSYrJfeMadE66JVnho6wwBmps5sPs%2B0PlSM44eHUMuMuIIdAU1maWlZOVVshXMr4laJc92Nimdwl5Y6wAWguJul65K30ohSau4e2TzhAJ2jVW%2B2SbxYI%2BUT%2FdXbTBzDpK0NC3nIRU29%2BRwGSB3yL8mpaLj8t1lPZX3P4WBe9gyvGJrnbHjDwKNnhHhafeNa3BbuE5lhIKGG%2BIQqU12eQ0Mpn4d6xM7RUjjEhmWtqH%2FxJ3g0Z7Yiy3h%2FxioNGJLw4yP6NNtp9IW%2B2bXveOlo8lmiI3ECEicLio3UEP2IVp9JWAezMymV1m9cRiCzS6oQ%2FIuHoHjOmFwCEsNfi5Sbv9eI3LssBpls7skskvJcRhypoKGJA9Hmudl6Ia4bFateqg9kvpEC3TGVmCCMM0trvGHr7SzCfsG16iMdGJcbM3D0zIg5q4zFbtOFiuF7%2B5oWzl3Oy%2FVKJHSSs9xr1%2F6XfKHOnx7Dc5BxCbKEPio%2F7dTKHSxi6o%2Bn7LnmxpYHAkD6kgqRpvhRD1UVmzL2yoaUwxdyMLrpDbftc8KLnbzp83f2BGwq%3D%5C%22%7D%22%2C%22biz_params%22%3A%22%7B%5C%22vid%5C%22%3A%5C%22XNDE1OTk3OTExNg%3D%3D%5C%22%2C%5C%22play_ability%5C%22%3A5376%2C%5C%22current_showid%5C%22%3A%5C%22335135%5C%22%2C%5C%22preferClarity%5C%22%3A4%2C%5C%22master_m3u8%5C%22%3A1%2C%5C%22media_type%5C%22%3A%5C%22standard%2Csubtitle%5C%22%2C%5C%22app_ver%5C%22%3A%5C%221.9.8%5C%22%7D%22%2C%22ad_params%22%3A%22%7B%5C%22vs%5C%22%3A%5C%221.0%5C%22%2C%5C%22pver%5C%22%3A%5C%221.9.8%5C%22%2C%5C%22sver%5C%22%3A%5C%222.0%5C%22%2C%5C%22site%5C%22%3A1%2C%5C%22aw%5C%22%3A%5C%22w%5C%22%2C%5C%22fu%5C%22%3A0%2C%5C%22d%5C%22%3A%5C%220%5C%22%2C%5C%22bt%5C%22%3A%5C%22pc%5C%22%2C%5C%22os%5C%22%3A%5C%22win%5C%22%2C%5C%22osv%5C%22%3A%5C%2210%5C%22%2C%5C%22dq%5C%22%3A%5C%22auto%5C%22%2C%5C%22atm%5C%22%3A%5C%22%5C%22%2C%5C%22partnerid%5C%22%3A%5C%22null%5C%22%2C%5C%22wintype%5C%22%3A%5C%22interior%5C%22%2C%5C%22isvert%5C%22%3A0%2C%5C%22vip%5C%22%3A0%2C%5C%22emb%5C%22%3A%5C%22AjEwMzk5OTQ3NzkCd3d3LnlvdWt1LmNvbQIv%5C%22%2C%5C%22p%5C%22%3A1%2C%5C%22rst%5C%22%3A%5C%22mp4%5C%22%2C%5C%22needbf%5C%22%3A2%7D%22%7D'
    headers = {'Referer': 'https://v.youku.com/v_show/id_XNDE1OTk3OTEwMA==.html?spm=a2h0j.11185381.listitem_page1.5!3~A&s=78808ead725845969b4e',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
             'Cookie':'__ysuid=1547439746320pPm; cna=FzbCFPXWOEYCAXF2UFa2UaQI; juid=01d159hcvc2io6; UM_distinctid=16dd3cfd56a3e1-0d791bbee85f2a-b363e65-144000-16dd3cfd56c83c; __aysid=1571216676305zoy; __ayft=1571548679831; __ayscnt=1; P_ck_ctl=EB99775FD6C492AC2CAF9F4321533A14; referhost=https%3A%2F%2Fwww.youku.com; yseid=1571548690615KsvmGC; yseidcount=5; ycid=0; __arycid=dz-3-00; __arcms=dz-3-00; _m_h5_tk=59a86b8b0156e9c83aebcc4d559375a2_1571561599427; _m_h5_tk_enc=1b84ac88c473fa6fcaeb9e18ced82f83; seid=01dnk19ip32eis; __arpvid=1571556918667fqQPYz-1571556918684; __aypstp=6; __ayspstp=25; seidtimeout=1571558722251; ypvid=1571556924981DyicXU; ysestep=5; yseidtimeout=1571564124982; ystep=20; __ayvstp=43; __aysvstp=367; isg=BMrKoeLAo6l-kC6Vivt3J1ViG7CsEysThymnOVQDwZ2oB2rBPEo-JaVlFTt-7Mat'
              }
    page = requests.get(url,headers=headers)
    pp = re.compile('"vid":(".*?")')
    col_num = pp.findall(page.text)
#     print(col_num)
    return col_num

# 返回弹幕列表
def get_dm(r):
    pp = re.compile('"content":(".*?")')
    dm_list = pp.findall(r.text)
    for i in dm_list:
        dms.append(i.replace('"', ''))
#     return dm_list

# url = 'https://service.danmu.youku.com/list?jsoncallback=jQuery111204898109498197434_1571188235234&mat=1&mcount=1&ct=1001&iid=1039994779&aid=335135&cid=97&lid=0&ouid=0&_=1571188235250'
url2 = 'https://service.danmu.youku.com/list?jsoncallback=jQuery111204898109498197434_1571188235234&mat={}&mcount=1&ct=1001&iid={}&aid=335135&cid=97&lid=0&ouid=0&_=1571188235250'

headers = {'referer': 'https://v.youku.com/v_show/id_XNDE1OTk3OTExNg==.html?spm=a2h0j.11185381.listitem_page1.5~A&s=78808ead725845969b4e',
          'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'}

num = get_collection()          #这里拿到所有集数id
for i in range(8):  #len(num)  #这里我只爬取8集
    print('爬取{}的弹幕'.format(num[i]))
    for j in range(40):     #每集取40分钟
        try:
            html = requests.get(url2.format(j ,num[i].replace('"' , "")),headers=headers) 
    #         print(html.text)
        except:
            print('爬取失败')
        print('\r'+'>'*j,end = '')
        get_dm(html)
        time.sleep(random.randint(2,5))
    
#词图分析
#处理中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']  #设置默认字体
plt.rcParams['axes.unicode_minus']=False   #解决保存图像显示的方格问题

# print(dms)
mycloud = WordCloud(font_path=font , width=800, height=400,background_color = "white").generate(' '.join(str(i) for i in dms))
plt.imshow(mycloud, interpolation="bilinear")
plt.axis('off') #去掉刻度轴
plt.show()
mycloud.to_file('wordcloud.png')   #保存生成的词云图
# if __name__=='__main__':
#     get_dm(html)
#     get_collection()
