import tkinter as tk
from tkinter import ttk
import math

import all_stats_display

from class_file.app import AppTopLevel
from class_file.stats_option import StatsOption
from class_file.stats import Stats

from function.set_widget_color import set_color, top_header_color, bg_color

condition_app = None
toggle = True
alpha = 95
canvas = None
stats_option = []
default_stats = None
row_offset = 0

each_option_option_combobox_var = None


def add_option(name, condition, stats):
    stats_option.append(StatsOption(name, condition, stats))
    draw_stats_option_window()


def reset_all_option():
    global condition_app, stats_option
    stats_option.clear()
    if condition_app is not None:
        condition_app.withdraw()
    all_stats_display.option_stats = Stats()


def toggle_option(option):
    if option.status.get():
        if type(option.stats) == list:
            stack = option.stack.get()
            if type(stack) != int:
                stack = 1
            else:
                stack -= 1
            all_stats_display.option_stats += option.stats[stack]
        else:
            all_stats_display.option_stats += option.stats
    else:
        if type(option.stats) == list:
            stack = option.stack.get()
            if type(stack) != int:
                stack = 1
            else:
                stack -= 1
            all_stats_display.option_stats -= option.stats[stack]
        else:
            all_stats_display.option_stats -= option.stats
    all_stats_display.draw_talent(False)


def draw_stats_option_window():
    global condition_app, stats_option, canvas, row_offset
    if condition_app is None:
        from main import app
        condition_app = AppTopLevel(app)
        condition_app.geometry('300x500+500+10')
        condition_app.attributes('-alpha', 0.95)
    else:
        condition_app.deiconify()

    # if nothing in stats_option destroy window and return
    if len(stats_option) <= 0:
        condition_app.withdraw()
        # condition_app.destroy()
        return

    row_offset = 0

    head_canvas = tk.Canvas(condition_app)
    head_canvas.configure(width=300, height=25, bd=0, bg=top_header_color, highlightthickness=0)
    head_canvas.place(x=0, y=0)

    canvas = tk.Canvas(condition_app)
    canvas.place(x=0, y=25)
    set_color(canvas, False)

    option_label = tk.Label(canvas)
    option_label.configure(text='Option', font=('TkDefaultFont', 12))
    option_label.place(x=10, y=row(0))
    set_color(option_label)
    current_row = 1

    last_name = ''
    for i, each_option in enumerate(stats_option):
        if last_name != each_option.name:
            each_option_name_label = tk.Label(canvas)
            each_option_name_label.configure(text=each_option.name)
            each_option_name_label.place(x=10, y=row(current_row))
            set_color(each_option_name_label)
            current_row += 1
            last_name = each_option.name

        each_option_option_checkbox = tk.Checkbutton(canvas)
        each_option_option_checkbox.configure(text=each_option.condition, variable=each_option.status,
                                              wraplength=250, justify=tk.LEFT,
                                              selectcolor=bg_color, command=lambda op=each_option: toggle_option(op))
        each_option_option_checkbox.place(x=20, y=row(current_row)-10)
        set_color(each_option_option_checkbox)

        if type(each_option.stats) == list:
            each_option_option_checkbox.configure(wraplength=200)
            each_option_option_checkbox.place(x=10, y=row(current_row) - 10, width=210)

            each_option_option_combobox_choices = list(range(1, len(each_option.stats)+1))
            stats_option[i].stack.set(1)
            each_option_stack_combobox = ttk.Combobox(canvas, textvariable=stats_option[i].stack,
                                                      values=each_option_option_combobox_choices)
            each_option_stack_combobox.place(x=240, y=row(current_row), width=50)
            set_color(each_option_option_checkbox)

        if len(each_option.condition) > 40:
            row_offset += math.ceil(len(each_option.condition)/40)
        current_row += 1

        condition_app.update()
        # condition_app.mainloop()


def set_alpha(value):
    if condition_app is not None:
        condition_app.attributes('-alpha', float(value) / 100)
        condition_app.update()
        global alpha
        alpha = value


def toggle_show():
    global condition_app, toggle
    if toggle:
        condition_app.withdraw()
        toggle = False
    else:
        condition_app.deiconify()
        toggle = True


def row(i):
    return 10 + (i * 30) + (row_offset*4)
