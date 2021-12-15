from os import link
from requests.models import CONTENT_CHUNK_SIZE
from tqdm import tqdm
import requests as rq
import json

class Youtube_dowloader:
    def __init__(self,yturl):
        self.yturl=yturl
        # self.r3=None
        self.url1="https://yt1s.com/api/ajaxSearch/index"
        self.url2="https://yt1s.com/api/ajaxConvert/convert"
        self.header={
        
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.5",
        "Connection":"keep-alive",
        "Content-Length":"65",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"_ga=GA1.2.866305265.1629990177; __atuvc=5%7C34",
        "DNT":"1",
        "Host":"yt1s.com",
        "Origin":"https://yt1s.com",
        "Referer":"https://yt1s.com/en37",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "X-Requested-With":"XMLHttpRequest"}
        



    def request_for_mp3(self):
        
        data = {"q": self.yturl,"vt": "mp3"}
        # request to youtube link link
        
        r = rq.post(self.url1,data=data)
        response =  json.loads(r.text)

        vid = response['vid']                # Get video id
        k=response['links']['mp3']['mp3128']['k']
        title = response['title']            # Get title
        a_rtist = response['a']
        data1={"vid":vid,"k":k}
        # print(title)
        print("uploader",a_rtist)
        r2= rq.post(self.url2,data=data1)
        res=json.loads(r2.text)
        # print(res)
        # request to download link
        
        dlink = res['dlink']
       
        return [dlink,title]
    def request_for_mp4(self,number):
        
        data = {"q": self.yturl,"vt": "mp3"}
        # request to youtube link link
        
        r = rq.post(self.url1,data=data)
        response =  json.loads(r.text)
        print(response)

        vid = response['vid']                # Get video id
        k=response['links']['mp4'][number]['k']
        title = response['title']            # Get title
        a_rtist = response['a']
        data1={"vid":vid,"k":k}
        print(title)
        print("uploader",a_rtist)
        r2= rq.post(self.url2,data=data1)
        res=json.loads(r2.text)
        # print(res)
        # request to download link
        
        dlink = res['dlink']
       
        return [dlink,title]
        

    def download_audio(self,r,title):
        # print(r.head)
        r = rq.get(r,stream=True)
        total = int(r.headers.get('content-length', 0))
        rcode=r.status_code
        if rcode==200:
        
            with open(title+".mp3","wb") as file:
                for data in tqdm(iterable=r.iter_content(chunk_size=1024),total=total/1024,unit="KB"):

                    file.write(data)
                    # bar.update(len(size))
            print("download complate" )
        else:
            print("download faild!...")
    def download_video(self,r,title):
        # print(r.head)
        r = rq.get(r,stream=True)
        total = int(r.headers.get('content-length', 0))
        rcode=r.status_code
        if rcode==200:
        
            with open(title+".mp4","wb") as file:
                for data in tqdm(iterable=r.iter_content(chunk_size=1024),total=total/1024,unit="KB"):

                    file.write(data)
                    # bar.update(len(size))
            print("download complate" )
        else:
            print("download faild!...")
if __name__=="__main__":
    url=input("Enter a youtube link here:")
    ut=Youtube_dowloader(url)
    for_downlod=input("if you want download video/audio please enter name:")
    if for_downlod=="audio":
        link=ut.request_for_mp3()
        dowlink=link[0]
        title=link[1]
        # print(title)
        # t=type(title)
        # print(t)
        # t=title.split("")
        # t=str(title)
        ut.download_audio(dowlink,title)

    elif for_downlod=="video":
        num=input("enter video queilty number\n 18 for 360p\n 22 for 720p\n 133 for 240p\n 135 for 480p\n 160 for 144p\n")
        link=ut.request_for_mp4(num)
        dowlink=link[0]
        title=link[1]
        # t=type(title)
        # t=title.split("")
        # t=str(title)
        ut.download_video(dowlink,title)
        


    else:
      exit()

    

   
    
    


