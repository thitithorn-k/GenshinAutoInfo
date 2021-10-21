from tkinter import Tk
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk
import numpy as np
import cv2
import data
from data import get_text
from data import get_keys
from all_stats_display import change_atf
from all_stats_display import remove_atf

from class_file.app import AppTopLevel

confirm_window_main = []


def artifact_confirm(atf_data, alpha, is_save=False):
    return_atf_data = {}
    bg_color = '#111111'
    fg_color = '#eeeeee'

    def confirm():
        change_check()
        change_atf(return_atf_data)
        cancel()

    def cancel():
        confirm_window_main.remove(list(confirm_window_main[a] for a, cw in enumerate(confirm_window_main) if cw[0] == confirm_window)[0])
        confirm_window.destroy()

    def remove_artifact():
        remove_atf(atf_data['part_name'], atf_data['owner'])
        cancel()

    def change_check():
        # check and add image to dataset
        if part_name_var.get() != atf_data['part_name']:
            add_to_data(atf_data['part_name_img_bw'], 'part_img_set', 'part_name', part_name_var.get())

        if get_keys(main_stat_name_var.get()) != atf_data['main_stat_name']:
            add_to_data(atf_data['main_stat_name_img_bw'], 'main_stat_img_set', 'main_stat_name', get_keys(main_stat_name_var.get()))

        if star_var.get() != atf_data['star']:
            pass
        if level_var.get() != atf_data['level']:
            pass
        for i, each_sub in enumerate(atf_data['sub_stat_name']):
            if get_keys(sub_stat_name_var[i].get()) != each_sub:
                add_to_data(atf_data['sub_stat_name_img_bw'][i], 'sub_stat_img_set', 'sub_stat_name', get_keys(sub_stat_name_var[i].get()))
        if asn_var.get() != atf_data['asn_name']:
            add_to_data(atf_data['asn_img_bw'], 'artifact_set_img_set', 'artifact_set_name', asn_var.get())

        # check data error
        return_atf_data['star'] = star_var.get()
        return_atf_data['level'] = level_var.get()
        return_atf_data['part_name'] = part_name_var.get()
        return_atf_data['main_stat_name'] = get_keys(main_stat_name_var.get())
        return_atf_data['main_stat_value'] = []
        return_atf_data['main_stat_value'].append(float(main_stat_value_text.get('1.0', 'end-1c')))
        return_atf_data['main_stat_value'].append(main_stat_value_percent_choices.index(main_stat_value_percent_var.get()))
        return_atf_data['sub_stat_name'] = []
        return_atf_data['sub_stat_value'] = []
        for i in range(4):
            if get_keys(sub_stat_name_var[i].get()) == 'none':
                print('con')
                continue
            return_atf_data['sub_stat_name'].append(get_keys(sub_stat_name_var[i].get()))
            return_atf_data['sub_stat_value'].append([float(sub_stat_value_text[i].get('1.0', 'end-1c')),
                                                      sub_stat_value_percent_choices.index(sub_stat_value_percent_var[i].get())])
        return_atf_data['asn_name'] = asn_var.get()

        # add old data
        return_atf_data['artifact_status_img'] = atf_data['artifact_status_img']
        return_atf_data['part_name_img_bw'] = atf_data['part_name_img_bw']
        return_atf_data['main_stat_name_img_bw'] = atf_data['main_stat_name_img_bw']
        return_atf_data['sub_stat_name_img_bw'] = atf_data['sub_stat_name_img_bw']
        return_atf_data['asn_img_bw'] = atf_data['asn_img_bw']
        if 'owner' in atf_data:
            return_atf_data['owner'] = atf_data['owner']

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

        add_data_window = AppTopLevel()
        add_data_window.title('add data confirm')
        add_data_window.geometry('300x200+500+10')
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

    confirm_window = AppTopLevel()
    confirm_window.title('Artifact status confirmation')
    confirm_window.geometry(f'650x{(image_h+110) if (image_h+110) > 400 else 390}+500+10')
    confirm_window.configure(bg=bg_color)
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('.', background=bg_color)
    s.configure('.', foreground=fg_color)

    head_label = tk.Label(confirm_window)
    head_label.place(x=10, y=row(0), height=24)
    head_label.configure(text='Artifact status confirm')
    set_color(head_label)

    confirm_btn = tk.Button(confirm_window)
    confirm_btn.place(x=10, y=row(1), width=100, height=24)
    confirm_btn.configure(text='Confirm')
    confirm_btn.configure(command=confirm)
    set_color(confirm_btn)

    cancel_btn = tk.Button(confirm_window)
    cancel_btn.place(x=116, y=row(1), width=100, height=24)
    cancel_btn.configure(text='Cancel')
    cancel_btn.configure(command=cancel)
    set_color(cancel_btn)

    if is_save:
        remove_btn = tk.Button(confirm_window)
        remove_btn.place(x=525, y=row(1), width=100, height=24)
        remove_btn.configure(text='Remove')
        remove_btn.configure(command=remove_artifact)
        set_color(remove_btn)

    im = Image.fromarray(artifact_status_img_rgb)
    imgtk = ImageTk.PhotoImage(image=im)
    artifact_img = tk.Label(confirm_window)
    artifact_img.place(x=10, y=70)
    artifact_img.configure(image=imgtk)

    part_label = tk.Label(confirm_window)
    part_label.place(x=256, y=row(3), height=24)
    part_label.configure(text='Gear part: ')
    set_color(part_label)

    c1x = 330
    c1w = 150
    c2x = c1x + c1w + 6
    c2w = 50
    c3x = c2x + c2w + 6
    c3w = 80

    part_x = 330
    part_choices = data.get_data('part_name')
    part_name = atf_data['part_name']
    part_name_var = tk.StringVar(confirm_window)
    part_name_var.set(part_name)
    part_dropdown = ttk.Combobox(confirm_window, textvariable=part_name_var, values=part_choices)
    part_dropdown.place(x=c1x, y=row(3), width=c1w, height=24)

    main_stat_label = tk.Label(confirm_window)
    main_stat_label.place(x=256, y=row(4), height=24)
    main_stat_label.configure(text='Main stat: ')
    set_color(main_stat_label)

    main_stat_x = 330
    main_stat_name_choices = data.get_data('main_stat_name')
    main_stat_name = atf_data['main_stat_name']
    main_stat_name_choices_lang = list(data.get_text(text) for text in main_stat_name_choices)
    main_stat_name_var = tk.StringVar(confirm_window)
    main_stat_name_var.set(get_text(main_stat_name))
    main_stat_dropdown = ttk.Combobox(confirm_window, textvariable=main_stat_name_var, values=main_stat_name_choices_lang)
    main_stat_dropdown.place(x=c1x, y=row(4), width=c1w, height=24)

    main_stat_value_text = tk.Text(confirm_window)
    main_stat_value_text.place(x=c2x, y=row(4), width=c2w, height=24)
    main_stat_value_text.insert(1.0, atf_data['main_stat_value'][0])
    main_stat_value_text.configure(pady=5)
    set_color(main_stat_value_text)

    main_stat_value_percent_choices = ['Point', '%']
    main_stat_value_percent_var = tk.StringVar(confirm_window)
    if atf_data['main_stat_value'][1] == 0:
        main_stat_value_percent_var.set(main_stat_value_percent_choices[0])
    else:
        main_stat_value_percent_var.set(main_stat_value_percent_choices[1])
    main_stat_value_percent_dropdown = ttk.Combobox(confirm_window, textvariable=main_stat_value_percent_var, values=main_stat_value_percent_choices)
    main_stat_value_percent_dropdown.place(x=c3x, y=row(4), width=c3w, height=24)

    star_label = tk.Label(confirm_window)
    star_label.place(x=256, y=row(5), height=24)
    star_label.configure(text=get_text('star'))
    set_color(star_label)

    star_choices = [2, 3, 4, 5]
    star = atf_data['star']
    star_var = tk.StringVar(confirm_window)
    star_var.set(star)
    star_dropdown = ttk.Combobox(confirm_window, textvariable=star_var, values=star_choices)
    star_dropdown.place(x=c1x, y=row(5), width=c1w, height=24)

    level_label = tk.Label(confirm_window)
    level_label.place(x=256, y=row(6), height=24)
    level_label.configure(text=get_text('level'))
    set_color(level_label)

    level_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    level = atf_data['level']
    level_var = tk.StringVar(confirm_window)
    level_var.set(level)
    level_dropdown = ttk.Combobox(confirm_window, textvariable=level_var, values=level_choices)
    level_dropdown.place(x=c1x, y=row(6), width=c1w, height=24)

    sub_stat_label = tk.Label(confirm_window)
    sub_stat_label.place(x=256, y=row(7), height=24)
    sub_stat_label.configure(text=get_text('sub_stat'))
    set_color(sub_stat_label)

    sub_stat_x = 330
    sub_stat_dropdown = []
    sub_stat_name_var = []
    sub_stat_value_text = []
    sub_stat_value_percent_var = []

    sub_stats_name = atf_data['sub_stat_name']
    sub_stat_name_choices = data.get_data('sub_stat_name').copy()
    sub_stat_name_choices.insert(0, 'none')
    sub_stat_name_choices_lang = list(data.get_text(text) for text in sub_stat_name_choices)
    for i in range(4):
        sub_stat_y = row(7+i)
        if i < len(sub_stats_name):
            sub_stat_name = sub_stats_name[i]
        else:
            sub_stat_name = 'none'
        sub_stat_name_var.append(tk.StringVar(confirm_window))
        sub_stat_name_var[i].set(get_text(sub_stat_name))
        sub_stat_dropdown.append(ttk.Combobox(confirm_window, textvariable=sub_stat_name_var[i], values=sub_stat_name_choices_lang))
        sub_stat_dropdown[i].place(x=c1x, y=sub_stat_y, width=c1w, height=24)

        sub_stat_value_text.append(tk.Text(confirm_window))
        sub_stat_value_text[i].place(x=c2x, y=sub_stat_y, width=c2w, height=24)
        if i < len(sub_stats_name):
            sub_stat_value_text[i].insert(1.0, atf_data['sub_stat_value'][i][0])
        else:
            sub_stat_value_text[i].insert(1.0, 0)
        sub_stat_value_text[i].configure(pady=5)
        set_color(sub_stat_value_text[i])

        sub_stat_value_percent_choices = ['Point', '%']
        sub_stat_value_percent_var.append(tk.StringVar(confirm_window))
        if i < len(sub_stats_name):
            if atf_data['sub_stat_value'][i][1] == 0:
                sub_stat_value_percent_var[i].set(sub_stat_value_percent_choices[0])
            else:
                sub_stat_value_percent_var[i].set(sub_stat_value_percent_choices[1])
        else:
            sub_stat_value_percent_var[i].set(sub_stat_value_percent_choices[0])
        sub_stat_value_percent_dropdown = ttk.Combobox(confirm_window, textvariable=sub_stat_value_percent_var[i],
                                          values=sub_stat_value_percent_choices)
        sub_stat_value_percent_dropdown.place(x=c3x, y=sub_stat_y, width=c3w, height=24)

    if 'sub_stat_y' in locals():
        asn_y = sub_stat_y + row(1) - 10
    else:
        asn_y = row(7)
    asn_label = tk.Label(confirm_window)
    asn_label.place(x=256, y=asn_y, height=24)
    asn_label.configure(text=get_text('artifact_set'))
    set_color(asn_label)

    asn_choices = sorted(data.get_data('artifact_set_name'))
    asn = atf_data['asn_name']
    asn_var = tk.StringVar(confirm_window)
    asn_var.set(asn)
    asn_dropdown = ttk.Combobox(confirm_window, textvariable=asn_var, values=asn_choices)
    asn_dropdown.place(x=c1x, y=asn_y, width=c1w + c2w + c3w + 12, height=24)

    confirm_window_main.append([confirm_window, True])
    set_alpha(alpha)
    confirm_window.attributes('-topmost', True)
    confirm_window.mainloop()


def set_alpha(value):
    if confirm_window_main is not []:
        for each in confirm_window_main:
            each[0].attributes('-alpha', float(value)/100)
            each[0].update()


def toggle_show():
    if confirm_window_main is not []:
        for each in confirm_window_main:
            if each[1]:
                each[0].withdraw()
                each[1] = False
            else:
                each[0].deiconify()
                each[1] = True


def row(i):
    return 10+(i*30)