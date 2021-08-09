from tkinter import Tk
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import numpy as np
import cv2
import data
from data import get_text

confirm_window_main = []


class App(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.bind('<Button-3>', self.clickwin)
        self.bind('<B3-Motion>', self.dragwin)

    def dragwin(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x+event.widget.winfo_rootx()-self.winfo_rootx()
        self._offsety = event.y + event.widget.winfo_rooty() - self.winfo_rooty()


def artifact_confirm(atf_data, alpha):
    bg_color = '#111111'
    fg_color = '#eeeeee'

    def confirm():
        change_check()

    def cancel():
        confirm_window_main.remove(confirm_window)
        confirm_window.destroy()

    def change_check():
        if main_stat_name_var.get() != atf_data['main_stat_name']:
            add_to_data(atf_data['main_stat_name_img_bw'], 'main_stat_img_set', 'main_stat_name', main_stat_name_var.get())

        if star_var.get() != atf_data['star']:
            pass
        if level_var.get() != atf_data['level']:
            pass
        for i, each_sub in enumerate(atf_data['sub_stat_name']):
            if sub_stat_name_var[i].get() != each_sub:
                pass

        atf_data['star'] = star_var.get()
        atf_data['level'] = level_var.get()
        # atf_data['part_name'] = part_name
        atf_data['main_stat_name'] = main_stat_name_var.get()
        atf_data['main_stat_value'][0] = float(main_stat_value_text.get('1.0', 'end-1c'))
        atf_data['main_stat_value'][1] = main_stat_value_percent_choices.index(main_stat_value_percent_var.get())
        for i, each_sub in enumerate(atf_data['sub_stat_name']):
            atf_data['sub_stat_name'][i] = sub_stat_name_var[i].get()
            atf_data['sub_stat_value'][i] = float(sub_stat_value_text[i].get('1.0', 'end-1c'))

    def set_color(obj):
        obj['bg'] = bg_color
        obj['fg'] = fg_color
        obj['highlightthickness'] = 0
        if hasattr(obj, 'activebackground'):
            obj['activebackground'] = bg_color
            obj['activeforeground'] = fg_color

    def add_to_data(image, img_set, list_of_name, name):

        def add_data_confirm():
            data.add_img_to_set(image, img_set, list_of_name, name)
            add_data_window.destroy()

        def add_data_cancel():
            add_data_window.destroy()

        add_data_window = App()
        add_data_window.title('add data confirm')
        add_data_window.geometry('300x200')
        add_data_window.configure(bg=bg_color)

        add_data_head_label = tk.Label(add_data_window)
        add_data_head_label.place(relx=.5, y=row(0), anchor=tk.N)
        add_data_head_label.configure(text=get_text('add_confirm_caution'))
        set_color(add_data_head_label)

        add_data_question_label = tk.Label(add_data_window)
        add_data_question_label.place(relx=.5, y=row(3), anchor=tk.N)
        add_data_question_label.configure(text=f'{get_text("add_confirm_question_start")} \'{get_text(name)}\'\n{get_text("add_confirm_question_end")}')
        set_color(add_data_question_label)

        add_data_confirm_btn = [None, None]
        add_data_confirm_btn[0] = tk.Button(add_data_window)
        add_data_confirm_btn[0].place(relx=.3, y=row(5), width=100, height=24, anchor=tk.N)
        add_data_confirm_btn[0].configure(text=get_text('yes'))
        add_data_confirm_btn[0].configure(command=add_data_confirm)
        set_color(add_data_confirm_btn[0])

        add_data_confirm_btn[1] = tk.Button(add_data_window)
        add_data_confirm_btn[1].place(relx=.7, y=row(5), width=100, height=24, anchor=tk.N)
        add_data_confirm_btn[1].configure(text=get_text('no'))
        add_data_confirm_btn[1].configure(command=add_data_cancel)
        set_color(add_data_confirm_btn[1])

        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=im)
        stat_img = tk.Label(add_data_window)
        stat_img.place(relx=.5, y=row(1.5), anchor=tk.N)
        stat_img.configure(image=imgtk)
        set_color(stat_img)

        add_data_window.attributes('-topmost', True)
        add_data_window.mainloop()

    artifact_status_img = atf_data['artifact_status_img']
    b, g, r = cv2.split(artifact_status_img)
    artifact_status_img_rgb = cv2.merge((r, g, b))
    image_h = artifact_status_img.shape[0]

    confirm_window = App()
    confirm_window.title('Artifact status confirmation')
    confirm_window.geometry(f'600x{image_h+90}')
    confirm_window.configure(bg=bg_color)
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('.', background=bg_color)
    s.configure('.', foreground=fg_color)

    head_label = tk.Label(confirm_window)
    head_label.place(x=10, y=row(0), height=24)
    head_label.configure(text='Artifact information confirm')
    set_color(head_label)

    confirm_btn = tk.Button(confirm_window)
    confirm_btn.place(x=10, y=row(1), width=100, height=24)
    confirm_btn.configure(text='Confirm')
    confirm_btn.configure(command=confirm)
    set_color(confirm_btn)

    cancel_btn = tk.Button(confirm_window)
    cancel_btn.place(x=116, y=row(1), width=100, height=24)
    cancel_btn.configure(text='Return')
    cancel_btn.configure(command=cancel)
    set_color(cancel_btn)

    im = Image.fromarray(artifact_status_img_rgb)
    imgtk = ImageTk.PhotoImage(image=im)
    artifact_img = tk.Label(confirm_window)
    artifact_img.place(x=10, y=70)
    artifact_img.configure(image=imgtk)

    main_stat_label = tk.Label(confirm_window)
    main_stat_label.place(x=256, y=row(4), height=24)
    main_stat_label.configure(text='Main stat: ')
    set_color(main_stat_label)

    main_stat_x = 330
    main_stat_name_choices = data.get_data('main_stat_name')
    main_stat_name = atf_data['main_stat_name']
    main_stat_name_var = tk.StringVar(confirm_window)
    main_stat_name_var.set(main_stat_name)
    main_stat_dropdown = tk.OptionMenu(confirm_window, main_stat_name_var, *main_stat_name_choices)
    main_stat_dropdown.place(x=330, y=row(4), width=100, height=24)
    set_color(main_stat_dropdown)

    main_stat_value_text = tk.Text(confirm_window)
    main_stat_value_text.place(x=main_stat_x + 106, y=row(4), width=50, height=24)
    main_stat_value_text.insert(1.0, atf_data['main_stat_value'][0])
    set_color(main_stat_value_text)

    main_stat_value_percent_choices = ['Point', '%']
    main_stat_value_percent_var = tk.StringVar(confirm_window)
    if atf_data['main_stat_value'][1] == 0:
        main_stat_value_percent_var.set(main_stat_value_percent_choices[0])
    else:
        main_stat_value_percent_var.set(main_stat_value_percent_choices[1])
    main_stat_value_percent_dropdown = tk.OptionMenu(confirm_window, main_stat_value_percent_var, *main_stat_value_percent_choices)
    main_stat_value_percent_dropdown.place(x=main_stat_x + 106 + 56, y=row(4), width=80, height=24)
    set_color(main_stat_value_percent_dropdown)

    star_label = tk.Label(confirm_window)
    star_label.place(x=256, y=row(5), height=24)
    star_label.configure(text='Stars: ')
    set_color(star_label)

    star_choices = {3, 4, 5}
    star = atf_data['star']
    star_var = tk.StringVar(confirm_window)
    star_var.set(star)
    star_dropdown = tk.OptionMenu(confirm_window, star_var, *star_choices)
    star_dropdown.place(x=330, y=row(5), width=100, height=24)
    set_color(star_dropdown)

    level_label = tk.Label(confirm_window)
    level_label.place(x=256, y=row(6), height=24)
    level_label.configure(text='level: ')
    set_color(level_label)

    level_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    level = atf_data['level']
    level_var = tk.StringVar(confirm_window)
    level_var.set(level)
    level_dropdown = tk.OptionMenu(confirm_window, level_var, *level_choices)
    level_dropdown.place(x=330, y=row(6), width=100, height=24)
    set_color(level_dropdown)

    sub_stat_label = tk.Label(confirm_window)
    sub_stat_label.place(x=256, y=row(7), height=24)
    sub_stat_label.configure(text='sub stat: ')
    set_color(sub_stat_label)

    sub_stat_x = 330
    sub_stat_dropdown = []
    sub_stat_name_var = []
    sub_stat_value_text = []
    sub_stat_value_percent_var = []
    for i, each_sub_stat in enumerate(atf_data['sub_stat_name']):
        sub_stat_y = row(7+i)
        sub_stat_name_choices = data.get_data('sub_stat_name')
        sub_stat_name = each_sub_stat
        sub_stat_name_var.append(tk.StringVar(confirm_window))
        sub_stat_name_var[i].set(sub_stat_name)
        sub_stat_dropdown.append(tk.OptionMenu(confirm_window, sub_stat_name_var[i], *sub_stat_name_choices))
        sub_stat_dropdown[i].place(x=330, y=sub_stat_y, width=100, height=24)
        set_color(sub_stat_dropdown[i])

        sub_stat_value_text.append(tk.Text(confirm_window))
        sub_stat_value_text[i].place(x=sub_stat_x + 106, y=sub_stat_y, width=50, height=24)
        sub_stat_value_text[i].insert(1.0, atf_data['sub_stat_value'][i][0])
        set_color(sub_stat_value_text[i])

        sub_stat_value_percent_choices = ['Point', '%']
        sub_stat_value_percent_var.append(tk.StringVar(confirm_window))
        if atf_data['sub_stat_value'][i][1] == 0:
            sub_stat_value_percent_var[i].set(sub_stat_value_percent_choices[0])
        else:
            sub_stat_value_percent_var[i].set(sub_stat_value_percent_choices[1])
        sub_stat_value_percent_dropdown = tk.OptionMenu(confirm_window, sub_stat_value_percent_var[i], *sub_stat_value_percent_choices)
        sub_stat_value_percent_dropdown.place(x=sub_stat_x + 106 + 56, y=sub_stat_y, width=80, height=24)
        set_color(sub_stat_value_percent_dropdown)

    confirm_window_main.append(confirm_window)
    set_alpha(alpha)
    confirm_window.attributes('-topmost', True)
    confirm_window.mainloop()


def set_alpha(value):
    if confirm_window_main is not []:
        for each in confirm_window_main:
            each.attributes('-alpha', float(value)/100)
            each.update()


def row(i):
    return 10+(i*30)