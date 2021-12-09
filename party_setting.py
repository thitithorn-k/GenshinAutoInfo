import tkinter as tk
from tkinter import ttk

from class_file.app import AppTopLevel
from function.set_widget import set_color, top_header_color, bg_color
from data import character_name

selected_member = []
toggle = True
party_app = None


def draw_window(app):
    global party_app
    party_app = AppTopLevel(app)
    party_app.geometry('120x190+10+210')

    canvas = tk.Canvas(party_app)
    canvas.configure(width=120, height=190, bd=0, bg=bg_color, highlightthickness=0)
    canvas.place(x=0, y=0)

    head_canvas = tk.Canvas(party_app)
    head_canvas.configure(width=120, height=25, bd=0, bg=top_header_color, highlightthickness=0)
    head_canvas.place(x=0, y=0)

    minimize_btn = tk.Button(head_canvas)
    minimize_btn.configure(text='-', command=lambda: toggle_show(0))
    minimize_btn.place(width=18, height=18, x=99, y=4)
    set_color(minimize_btn)

    head_label = tk.Label(party_app)
    head_label.configure(text='Party Member')
    head_label.place(x=10, y=30)
    set_color(head_label)

    for i in range(4):
        party_combobox_choices = sorted(character_name)
        party_combobox_choices.insert(0, 'None')
        for j in range(i):
            if selected_member[j] and selected_member[j].get() != 'None':
                party_combobox_choices.remove(selected_member[j].get())
        selected_member.append(tk.StringVar(party_app))
        selected_member[i].set(party_combobox_choices[0])
        party_combobox = ttk.Combobox(canvas, textvariable=selected_member[i], values=party_combobox_choices, width=12)
        party_combobox.place(x=10, y=55+(i*30))


def toggle_show(fix_stat=-1):
    global party_app, toggle
    if toggle or (fix_stat == 0 and fix_stat != 1):
        party_app.withdraw()
        toggle = False
    else:
        party_app.deiconify()
        toggle = True


