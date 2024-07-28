import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image


class NewsApp:
    def __init__(self):
        # fetch data
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&apiKey=264bb69410ff4cb8902b319e339a6c8b').json()
        self.load_gui()
        self.load_news_item(0)
        # Initial GUI load
        # load the 1 set news item

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.title("News App by Naman Pamecha")
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():  # pack_slaves are basically the buttons and the gui items you use are known as pack slaves
            i.destroy()

    def load_news_item(self, index):
        # clear the screen for the new news item
        self.clear()

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = "https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg"
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=photo)
        label.pack()
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify="center")
        heading.pack(pady=(10, 20))
        heading.config(font=("verdana", 15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350,
                        justify="center")
        details.pack(pady=(2, 20))
        details.config(font=("verdana", 12))

        frame = Frame(self.root, bg="black")
        frame.pack(expand=True, fill=BOTH)
        if index != 0:
            prev = Button(frame, text="Prev", width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text="Read More", width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text="Next", width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=RIGHT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


NewsApp()
