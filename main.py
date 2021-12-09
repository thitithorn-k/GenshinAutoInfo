import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from PIL import ImageTk, Image
import cv2
from data import get_text
import os
import keyboard

from scan import run
import stats_confirm
import all_stats_display
import condition_option
import party_setting

from class_file.app import AppMain

from function.set_widget import set_color, bg_color, fg_color

alpha = 95
app = None
toggle = True
toggle_save = None


def toggle_show(self):
    global app, toggle, toggle_save
    import threading
    toggle = not toggle
    if not toggle:
        toggle_save = app.winfo_geometry()
        app.overrideredirect(False)
        app.iconify()

        stats_confirm.toggle_show(0)
        all_stats_display.toggle_show(0)
        condition_option.toggle_show(0)
        party_setting.toggle_show(0)

        threading.Thread(target=wait_for_toggle_show).start()
        # wait_for_toggle_show()


def wait_for_toggle_show():
    global app, toggle, toggle_save
    from time import sleep
    while True:
        if app.state() != 'normal' and not toggle:
            sleep(0.5)
        else:
            app.geometry(toggle_save)
            toggle = True
            app.deiconify()
            app.overrideredirect(True)
            stats_confirm.toggle_show(1)
            all_stats_display.toggle_show(1)
            condition_option.toggle_show(1)
            party_setting.toggle_show(1)
            break


def scan(sample=False):
    im = run(sample)
    if type(im) is int:
        print('error')
    else:
        res = stats_confirm.artifact_confirm(im, alpha)
        print('res=', res)


def scan_sample():
    scan(True)


def exit_program():
    app.destroy()


def main():

    def set_alpha(value):
        global alpha
        alpha = value
        app.attributes('-alpha', float(value) / 100)
        app.update()
        stats_confirm.set_alpha(value)
        all_stats_display.set_alpha(value)
        condition_option.set_alpha(value)

    global app
    app = AppMain()
    app.geometry('120x190+10+10')
    app.title('Genshin Auto Info')
    app.configure(bg=bg_color)
    app.option_add("*TCombobox*Listbox*Background", bg_color)
    app.option_add("*TCombobox*Listbox*Foreground", fg_color)
    print('this app= ', app)

    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('.', background=bg_color)
    s.configure('.', foreground=fg_color)
    s.configure('TCombobox', fieldbackground=bg_color, foreground=fg_color, fieldforeground=bg_color,
                background=bg_color, highlightthickness=0)

    head_label = tk.Label(app)
    head_label.place(x=10, y=10, width=100, height=24)
    head_label.configure(text='Genshin Auto Info')
    set_color(head_label)

    run_btn = tk.Button(app)
    run_btn.place(x=10, y=40, width=100, height=24)
    run_btn.configure(text=get_text('scan'))
    run_btn.configure(command=scan)
    set_color(run_btn)

    run_sample_btn = tk.Button(app)
    run_sample_btn.place(x=10, y=70, width=100, height=24)
    run_sample_btn.configure(text=get_text('scan_sam'))
    run_sample_btn.configure(command=scan_sample)
    set_color(run_sample_btn)

    about_btn = tk.Button(app)
    about_btn.place(x=10, y=100, width=100, height=24)
    about_btn.configure(text=get_text('about'))
    # about_btn.configure(command=scan_sample)
    set_color(about_btn)

    close_btn = tk.Button(app)
    close_btn.place(x=10, y=130, width=100, height=24)
    close_btn.configure(text=get_text('close'))
    close_btn.configure(command=exit_program)
    set_color(close_btn)

    alpha_set_scale = ttk.Scale(app, from_=30, to=100)
    alpha_set_scale.place(x=10, y=160, width=100)
    alpha_set_scale.configure(length='97')
    alpha_set_scale.configure(takefocus='')
    alpha_set_scale.configure(orient=tk.HORIZONTAL)
    alpha_set_scale.set(95)
    alpha_set_scale.configure(command=set_alpha)

    app.attributes('-alpha', 0.95)
    app.update()
    all_stats_display.main(app)
    condition_option.draw_stats_option_window(app)
    party_setting.draw_window(app)

    app.mainloop()


if __name__ == '__main__':
    keyboard.on_press_key("F12", toggle_show)
    main()






