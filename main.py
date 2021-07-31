import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from PIL import ImageTk, Image
import cv2

from scan import run
from stats_confirm import show


class App(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-3>', self.clickwin)
        self.bind('<B3-Motion>', self.dragwin)

    def dragwin(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x
        self._offsety = event.y


def scan():
    run()


def scan_sample():
    im = run(True)
    # show(im)


def set_alpha(value):
    app.attributes('-alpha', float(value)/100)
    app.update()


def quit():
    app.destroy()

bg_color = '#333333'
fg_color = '#eeeeee'

app = App()
app.geometry('120x190')
app.configure(bg=bg_color)
s = ttk.Style()
s.theme_use('winnative')
s.configure('.', background=bg_color)
s.configure('.', foreground=fg_color)


head_label = tk.Label(app)
head_label.place(x=10, y=10, width=100, height=24)
head_label.configure(text='Genshin Auto Info')
head_label.configure(bg=bg_color)
head_label.configure(fg=fg_color)

run_btn = tk.Button(app)
run_btn.place(x=10, y=40, width=100, height=24)
run_btn.configure(text='Scan')
run_btn.configure(command=scan)
run_btn.configure(bg=bg_color)
run_btn.configure(fg=fg_color)

run_sample_btn = tk.Button(app)
run_sample_btn.place(x=10, y=70, width=100, height=24)
run_sample_btn.configure(text='Scan Sample')
run_sample_btn.configure(command=scan_sample)
run_sample_btn.configure(bg=bg_color)
run_sample_btn.configure(fg=fg_color)

about_btn = tk.Button(app)
about_btn.place(x=10, y=100, width=100, height=24)
about_btn.configure(text='About')
# about_btn.configure(command=scan_sample)
about_btn.configure(bg=bg_color)
about_btn.configure(fg=fg_color)

close_btn = tk.Button(app)
close_btn.place(x=10, y=130, width=100, height=24)
close_btn.configure(text='Close')
close_btn.configure(command=quit)
close_btn.configure(bg=bg_color)
close_btn.configure(fg=fg_color)

alpha_set_scale = ttk.Scale(app, from_=30, to=100)
alpha_set_scale.place(x=10, y=160, width=100)
alpha_set_scale.configure(length='97')
alpha_set_scale.configure(takefocus='')
alpha_set_scale.configure(orient=tk.HORIZONTAL)
alpha_set_scale.set(100)
alpha_set_scale.configure(command=set_alpha)

app.attributes('-topmost', True)
app.attributes('-alpha', 1)

app.mainloop()





