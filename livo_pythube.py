from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = entry.get()
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Livo-pytube video downloader")

label = tk.Label(root, text="Enter the link of the Youtube video you want to download below : ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Download Now!", command=download_video)
button.pack()

root.mainloop()