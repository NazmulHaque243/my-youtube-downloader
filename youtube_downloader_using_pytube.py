from pytube import YouTube, streams
from tqdm import tqdm
import os
banner="""
__   __         _____      _
\ \ / /__  _   |_   _|   _| |__   ___
 \ V / _ \| | | || || | | | '_ \ / _ \
  | | (_) | |_| || || |_| | |_) |  __/
  |_|\___/ \__,_||_| \__,_|_.__/ \___|

 ____                      _                 _           _ _
|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __| | |
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__| | |
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |  |_|_|
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|  (_|_)

"""
# from pytube.cli import on_progress


def on_progress(stream,chunk,bytes_remaining):
    total=stream.filesize
    for data in tqdm(iterable=chunk,total=total,unit="kb"):
        pass

    
def on_complate(stream,file_path):
    print("download complate")







def youtube_downloader(links_of):
    
    # youtube_link=links_of[urls]
    yt=YouTube(links_of,on_progress_callback=on_progress)
    print("please wait.....")
    # print("video clips")
    print(f"Title: {yt.title}")
    print("wait for more information...")
    for index,i in enumerate(yt.streams):
        if i.type=="video":
            print("---------------------video-------------------")
            print(f"{index}: {i.resolution}{round(i.filesize/(1024*1024),2)}MB")
        else:
            print("---------------------audio-------------------")
            print(f"{index}: {i.abr}{round(i.filesize/(1024*1024),2)}MB")

            
    inpu=int(input("Enter number for download:"))
    s=yt.streams[inpu]
    dirs=os.getcwd()+r"\ntube"
    if not dirs:
        os.mkdir(dirs)

    s.download(dirs)





if __name__=="__main__":
    while True:
        print(banner)
        print("ready to download video from youtube enter link or enter exit to terminate")
        urls=(input("enter a yotube video link:"))
        if urls=="exit":
            exit()
        youtube_downloader(urls)
        
