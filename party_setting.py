import tkinter as tk

from class_file.app import AppTopLevel
from function.set_widget_color import set_color, top_header_color


def draw_window(app):
    party_app = AppTopLevel(app)
    party_app.geometry('120x190+10+210')

    head_canvas = tk.Canvas(party_app)
    head_canvas.configure(width=300, height=25, bd=0, bg=top_header_color, highlightthickness=0)
    head_canvas.place(x=0, y=0)

    head_label = tk.Label(party_app)
    head_label.configure(text='Party Member')
    head_label.place(x=10, y=30)
    set_color(head_label)