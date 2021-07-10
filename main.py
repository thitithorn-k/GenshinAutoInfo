from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from PIL import ImageTk, Image
import cv2

# from reader import Read

from scan import run
from stats_confirm import show


# def read_image():
#     read()


def scan():
    run()


def scan_sample():
    im = run(True)
    # show(im)


GUI = Tk()
GUI.geometry('200x100')
# Read_Btn = Button(GUI, text='read', command=read_image)
Scan_Btn = Button(GUI, text='Scan', command=scan)
Scan_sample_btn = Button(GUI, text='Scan Sample', command=scan_sample)

canvas = Canvas(GUI)

img = ImageTk.PhotoImage(Image.open('./data/red.png'))
canvas.create_image(20, 20, image=img)

# Read_Btn.pack()
Scan_Btn.pack()
Scan_sample_btn.pack()
canvas.pack()
GUI.mainloop()





