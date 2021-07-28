from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from PIL import ImageTk, Image
import cv2

from scan import run
from stats_confirm import show


def scan():
    run()

def scan_sample():
    im = run(True)
    # show(im)


app = Tk()
app.geometry('200x100')
# Read_Btn = Button(app, text='read', command=read_image)
Scan_Btn = Button(app, text='Scan', command=scan)
Scan_sample_btn = Button(app, text='Scan Sample', command=scan_sample)

canvas = Canvas(app)

img = ImageTk.PhotoImage(Image.open('./data/red.png'))
canvas.create_image(20, 20, image=img)

# Read_Btn.pack()
Scan_Btn.pack()
Scan_sample_btn.pack()
canvas.pack()

app.attributes('-topmost', True)
app.attributes('-alpha', 0.8)

app.mainloop()





