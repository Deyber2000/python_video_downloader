#importing packages
from tkinter import *
from pytube import YouTube

#creating tkinter window
root = Tk()
#set position and size to render window
root.geometry('500x300')
root.resizable(0,0)
#set title
root.title("Ramon's video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
#store link
link = StringVar()
#create field to enter video link
Label(root, text = 'Enter Link: ', font = 'arial 15 bold').place(x= 160 , y = 60)
#input text field
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
SAVE_PATH = "/home/ramon/Holberton/python_video_downloader"
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(SAVE_PATH)
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()

