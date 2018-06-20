from pytube import YouTube
import os

url = input("input the youtube url : ")

try:
    yt = YouTube(url)

    # a perfect balance of simplicity versus flexibility
    yt.streams.filter(progressive=True).filter(subtype="mp4").order_by("resolution").desc().first().download()

    print("Done! Check your file at {}.".format(os.getcwd()))

except:
    print("the url is wrong!")