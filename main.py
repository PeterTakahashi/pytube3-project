import csv
from pytube import YouTube


def download(url, index):
    yt = YouTube(url)
    print(str(index) + "番目の動画をダウンロードします。")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download('./news', str(index))


with open('youtube_links.csv') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        url = row[0]
        print("start download")
        download(url, index)
        print("completed download")
