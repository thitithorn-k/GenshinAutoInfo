from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Toplevel
from PIL import ImageTk, Image
import numpy as np
import cv2


def show(img):
    def confirm():
        pass

    def cancel():
        pass

    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))

    GUI = Toplevel()
    GUI.title('Artifact status confirmation')
    GUI.geometry('400x100')
    confirm_btn = Button(GUI, text='Confirm', command=confirm)
    cancel_btn = Button(GUI, text='Return', command=cancel)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)

    Label(GUI, image=imgtk).pack()

    # Read_Btn.pack()
    confirm_btn.pack()
    cancel_btn.pack()

    GUI.mainloop()