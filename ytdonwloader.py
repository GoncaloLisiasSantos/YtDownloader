from pytubefix import YouTube

url = input("Enter the URL of the video: ")
yt = YouTube(url)
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)
print("Description: ", yt.description)


ys = yt.streams.get_highest_resolution()
ys.download()
