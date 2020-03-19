from tkinter import *
from PIL import Image, ImageTk

photo = PhotoImage(file="portee.jpg")
window = Tk()
window.geometry("720x480")

load = Image.open("portee.jpg")
render = ImageTk.PhotoImage(load)
img = Label(self, image=render)
img.image = render
img.place(x=0, y=0)


canvas = Canvas(window,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
