from pytube import YouTube
def Download(link):
    youtubeObject=YouTube (link)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

    print("Download is completed successfully")

Link = input("Enter the YouTube video URL: ")
Download (Link)
