from tkinter import *


import os
import sys

from pytube import YouTube


def download():
    global input_link
    string = input_link.get()
    print("link: ", string)

    yt = YouTube(string)
    yd = yt.streams.get_highest_resolution()
    print('Descarga en curso')

    dir_name = 'videos'
    path = sys.path[0]
    yd.download(output_path=f'{path}/{dir_name}')
    print('Descarga Terminada')
        



def close_window():
    root.destroy()


root = Tk()
root.geometry('500x180')
root.title('Simple Youtube Converter')


logo = PhotoImage(file='assets/logo.png')
root.iconphoto(False, logo)

input_link = Entry(root, width=50)
label_link = Label(root, text="Link: ")





    
button_downlaod = Button(root, text="Download", command=download)


label_link.pack()
input_link.pack()

input_link.focus_set()
button_downlaod.pack(pady=25)


root.mainloop()
