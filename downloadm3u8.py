import requests
import random
import os


with open(os.getcwd()+"\\url.txt", "r",encoding='utf-8') as urls:
    for url in urls.readlines():
        print(url)
        cookies = requests.cookies.RequestsCookieJar()
        cookies.set("language", "cn_CN", domain=".p06.rocks", path="/")
        randomIP = str(random.randint(0, 255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',"Accept-Language":"zh-CN,zh;",'X-Forwarded-For': randomIP}
        try:
            response=requests.get(url,headers=headers,timeout=15)
        except requests.exceptions.RequestException:
            pass
        with open(os.getcwd()+"\\temp.txt","w",encoding='utf-8') as f:
            f.write(response.text)
        with open(os.getcwd()+"\\temp.txt", "r",encoding='utf-8') as f:
            for line in f.readlines():
                if line.find('<title>')==-1:
                    pass
                else:  
                    title=line.replace('<title>','').replace(' ','')                
                if line.find('img2')==-1:
                    pass
                else:
                    m3u8=line.replace('<video id="player_one" class="video-js vjs-sublime-skin vjs-16-9" preload="auto" width="100%"  controls poster="https://img2.t6k.co/thumb/','').replace('.jpg" data-setup=\'{}\'>','').replace(" ","").replace("\t","").strip()
                    m3u8url='https://ccn.killcovid2021.com//m3u8/'+m3u8+'/'+m3u8+'.m3u8'
                    with open(os.getcwd()+"\\m3u8url.txt","a",encoding='utf-8') as f:
                        f.write(m3u8url+','+title)
    print("所有视频下载地址获取完成，接下来可以把存在m3u8url.txt中的结果复制到M3U8Dwonloader中下载了")
