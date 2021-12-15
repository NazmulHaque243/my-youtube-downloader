from pytube import YouTube, streams
from pytube.cli import on_progress





def youtube_downloader(links_of):
    
    # youtube_link=links_of[urls]
    yt=YouTube(links_of,on_progress_callback=on_progress)
    print("please wait.....")
    print("video clips")
    print(yt.title)
    print("wait for information...")
    for index,i in enumerate(yt.streams):
        if i.type=="video":
            print(f"{index}: {i.resolution}{i.filesize//1024}kb")
        else:
            print(f"{index}: {i.abr}{i.filesize}kb")

            
    inpu=int(input("Enter number for download:"))
    s=yt.streams[inpu]
    s.download()

# driver.close()
if __name__=="__main__":
    urls=(input("enter a yotube video link:"))
    youtube_downloader(urls)