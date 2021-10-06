import openpyxl
import tkinter as tk
from tkinter import ttk

app = None
artifact = [None]*5

stat_offset = [
    'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X'
]
char_level_offset = [
    '1', '20', '20+', '40', '40+', '50', '50+', '60', '60+', '70', '70+', '80', '80+', '90'
]
weapons_level_offset = [
    '1', '5', '10', '15', '20', '20+', '25', '30', '35', '40', '40+', '45', '50', '50+',
    '55', '60', '60+', '65', '70', '70+', '75', '80', '80+', '85', '90'
]
weapons_type = ['All', 'Sword', 'Claymore', 'Polearm', 'Bow', 'Catalyst']
character_name = [
    'Zhongli',
    'Ganyu',
    'Klee',
    'Keqing',
    'Kaeya',
    'Amber',
    'Barbara',
    'Beidou',
    'Bennett',
    'Chongyun',
    'Diluc',
    'Fischl',
    'Jean',
    'Lisa',
    'Mona',
    'Ningguang',
    'Noelle',
    'Qiqi',
    'Razor',
    'Sucrose',
    'Traveler',
    'Venti',
    'Xiangling',
    'Xiao',
    'Xingqiu',
    'Tartaglia',
    'Diona',
    'Xinyan',
    'Albedo',
    'Rosaria',
    'Hu Tao',
    'Yanfei',
    'Eula',
    'Kaedehara Kazuha',
    'Kamisato Ayaka',
    'Yoimiya',
    'Sayu',
    'Raiden Shogun',
    'Sangonomiya Kokomi',
    'Aloy',
    'Kujou Sara'
]

selected_character = None
data_file = openpyxl.open('./data/characters_weapons.xlsx')
weapons_data = None


class App(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
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
        self._offsetx = event.x + event.widget.winfo_rootx() - self.winfo_rootx()
        self._offsety = event.y + event.widget.winfo_rooty() - self.winfo_rooty()


class ArtifactStat:
    def __init__(self):
        self.ATK = []
        self.ATK_p = []
        self.CRIT_R = []
        self.CRIT_D = []
        self.EM = []
        self.HP = []
        self.HP_p = []
        self.DEF = []
        self.DEF_p = []
        self.PDMG_p = []
        self.EDMG_p = []
        self.HEAL_p = []
        self.SHIELD_p = []
        self.ER_p = []


class Stats:
    def __init__(self):
        self.ATK = []
        self.ATK_p = []
        self.CRIT_R = []
        self.CRIT_D = []
        self.EM = []
        self.HP = []
        self.HP_p = []
        self.DEF = []
        self.DEF_p = []
        self.PDMG_p = []
        self.EDMG_p = []
        self.HEAL_p = []
        self.SHIELD_p = []
        self.ER_p = []


class Character:
    def __init__(self, HP, ATK, DEF, CR, CD, ATK_p, EM, HP_p, DEF_p,
                 HEAL_p, PDMG_p, EDMG_p, BSCONDUCT, BOVERLOAD, BELECTROCH, BSWIRL,
                 BSHATTER, BCRYSTALIZE, E_RECHARGE, WEAPON_TYPE):
        self.HP = HP  # 0
        self.ATK = ATK  # 1
        self.DEF = DEF  # 2
        self.CR = CR  # 3
        self.CD = CD  # 4
        self.ATK_p = ATK_p  # 5
        self.EM = EM  # 6
        self.HP_p = HP_p  # 7
        self.DEF_p = DEF_p  # 8
        self.HEAL_p = HEAL_p  # 9
        self.PDMG_p = PDMG_p  # 10
        self.EDMG_p = EDMG_p  # 11
        self.BSCONDUCT = BSCONDUCT  # 12
        self.BOVERLOAD = BOVERLOAD  # 13
        self.BELECTROCH = BELECTROCH  # 14
        self.BSWIRL = BSWIRL  # 15
        self.BSHATTER = BSHATTER  # 16
        self.BCRYSTALIZE = BCRYSTALIZE  # 17
        self.E_RECHARGE = E_RECHARGE  # 18
        self.WEAPON_TYPE = WEAPON_TYPE  # 19

class Weapon:
    def __init__(self):
        pass


def change_atf(atf_data):
    global artifact
    part_name = atf_data['part_name']
    if part_name == 'flower':
        artifact[0] = atf_data
    elif part_name == 'plume':
        artifact[1] = atf_data
    elif part_name == 'sands':
        artifact[2] = atf_data
    elif part_name == 'goblet':
        artifact[3] = atf_data
    elif part_name == 'circlet':
        artifact[4] = atf_data
    else:
        print(f'change atf error. part name not match ({part_name})')


def load_weapons_data():
    weapons = data_file['Weapons']
    r_count = 0
    row = 2 + (27 * r_count)
    weapons_data = []
    while weapons[f'A{row}'].value is not None:
        weapons_data.append([weapons[f'A{row}'].value, weapons[f'B{row}'].value, weapons[f'C{row}'].value, row])
        r_count += 1
        row = 2 + (27 * r_count)
    return weapons_data  # (weapon name, type, rarity, row of data)


def get_character_info(char_name, level):
    characters = data_file['Characters']
    row = 2 + (character_name.index(char_name)*16) + char_level_offset.index(level)
    stats = []
    for each_stat in stat_offset:
        if each_stat in ['P', 'Q', 'R', 'S', 'T', 'U']:
            value = characters[f'{each_stat}{2 + char_level_offset.index(level)}'].value
        if each_stat == 'X':
            value = characters[f'X{2 + (character_name.index(char_name)*16)}'].value
        else:
            value = characters[f'{each_stat}{row}'].value
        if value is None:
            value = '0'
        stats.append(value)
    return(Character(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6],
                     stats[7], stats[8], stats[9], stats[10], stats[11], stats[12], stats[13],
                     stats[14], stats[15], stats[16], stats[17], stats[18], stats[19]))


def set_alpha(value):
    app.attributes('-alpha', float(value) / 100)
    app.update()


# draw stats window
def draw_window():



    def set_color(obj):
        bg_color = '#111111'
        fg_color = '#eeeeee'
        obj['bg'] = bg_color
        obj['fg'] = fg_color
        obj['highlightthickness'] = 0
        if hasattr(obj, 'activebackground'):
            obj['activebackground'] = bg_color
            obj['activeforeground'] = fg_color

    bg_color = '#111111'
    fg_color = '#eeeeee'
    global weapons_data
    # weapon_type_var = None

    global app
    app = App()
    app.geometry('410x300+140+10')
    app.configure(bg=bg_color)
    app.option_add("*TCombobox*Listbox*Background", bg_color)
    app.option_add("*TCombobox*Listbox*Foreground", fg_color)

    # Select Character
    def character_change(self):
        global selected_character
        selected_character = get_character_info(char_name_var.get(), char_level_var.get())
        print(selected_character.HP)

        _weapons_name = sorted([weapons_data[i][0] for i, _ in enumerate(weapons_data) if weapons_data[i][1] == selected_character.WEAPON_TYPE])
        if weapon_name_var.get() not in _weapons_name and len(_weapons_name) > 0:
            weapon_name_var.set(_weapons_name[0])
        weapon_name_dropdown.config(value=_weapons_name)

    character_label = tk.Label(app)
    character_label.place(x=10, y=10, height=24)
    character_label.configure(text='Character')
    set_color(character_label)

    char_name_choices = sorted(character_name)
    char_name_var = tk.StringVar(app)
    char_name_var.set(char_name_choices[0])
    # char_name_dropdown = tk.OptionMenu(app, char_name_var, *char_name_choices, command=character_change)
    char_name_dropdown = ttk.Combobox(app, textvariable=char_name_var, values=char_name_choices)
    char_name_dropdown.bind('<<ComboboxSelected>>', character_change)
    char_name_dropdown.place(x=70, y=10, width=150, height=24)

    char_level_choices = char_level_offset
    char_level_var = tk.StringVar(app)
    char_level_var.set(char_level_offset[len(char_level_offset) - 1])
    char_level_dropdown = ttk.Combobox(app, textvariable=char_level_var, values=char_level_choices)
    char_level_dropdown.bind('<<ComboboxSelected>>', character_change)
    char_level_dropdown.place(x=230, y=10, width=60, height=24)

    def weapon_name_changed(self):
        # weapon_level_dropdown['menu'].delete(0, tk.END)
        rarity = [weapons_data[i][2] for i, _ in enumerate(weapons_data) if weapons_data[i][0] == weapon_name_var.get()]
        if len(rarity) > 0 and (rarity[0] == 1 or rarity[0] == 2):
            weapons_level = weapons_level_offset[0:19]
            if weapon_level_var.get() not in weapons_level:
                weapon_level_var.set(weapons_level[len(weapons_level)-1])
        else:
            weapons_level = weapons_level_offset
        weapon_level_dropdown.config(value=weapons_level)
        # for each_level in weapons_level:
        #     weapon_level_dropdown['menu'].add_command(label=each_level,
        #                                              command=lambda value=each_level: weapon_level_var.set(value))

    weapon_label = tk.Label(app)
    weapon_label.place(x=10, y=40, height=24)
    weapon_label.configure(text='Weapon')
    set_color(weapon_label)

    weapons_name = [weapons_data[i][0] for i, _ in enumerate(weapons_data)]
    weapon_name_choices = sorted(weapons_name)
    weapon_name_var = tk.StringVar(app)
    weapon_name_var.set(weapon_name_choices[0])
    weapon_name_dropdown = ttk.Combobox(app, textvariable=weapon_name_var, values=weapon_name_choices)
    weapon_name_dropdown.bind('<<ComboboxSelected>>', weapon_name_changed)
    weapon_name_dropdown.place(x=70, y=40, width=150, height=24)

    weapon_level_choices = weapons_level_offset
    weapon_level_var = tk.StringVar(app)
    weapon_level_var.set(weapons_level_offset[len(weapons_level_offset) - 1])
    weapon_level_dropdown = ttk.Combobox(app, textvariable=weapon_level_var, values=weapon_level_choices)
    weapon_level_dropdown.place(x=230, y=40, width=60, height=24)

    # refresh weapon name
    character_change(None)

    app.attributes('-topmost', True)
    app.attributes('-alpha', 0.95)
    app.mainloop()


def main():
    global weapons_data
    weapons_data = load_weapons_data()
    draw_window()