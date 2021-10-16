import openpyxl
import tkinter as tk
from tkinter import ttk


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
        self.CR = []
        self.CD = []
        self.EM = []
        self.HP = []
        self.HP_p = []
        self.DEF = []
        self.DEF_p = []
        self.PDMG = []
        self.ANEMO_DMG = []
        self.GEO_DMG = []
        self.ELECTRO_DMG = []
        self.HYDRPO_DMG = []
        self.PYRO_DMG = []
        self.CRYO_DMG = []
        self.HEAL = []
        self.SHIELD = []
        self.ER = []

    def print_log(self):
        print(f'ATK={self.ATK}\n'
              f'ATK_p={self.ATK_p}\n'
              f'CR={self.CR}\n'
              f'CD={self.CD}\n'
              f'EM={self.EM}\n'
              f'HP={self.HP}\n'
              f'HP_p={self.HP_p}\n'
              f'DEF={self.DEF}\n'
              f'DEF_p={self.DEF_p}\n'
              f'PDMG_p={self.PDMG}\n'
              f'ANEMO_DMG={self.ANEMO_DMG}\n'
              f'GEO_DMG={self.GEO_DMG}\n'
              f'ELECTRO_DMG={self.ELECTRO_DMG}\n'
              f'HYDRO_DMG={self.HYDRPO_DMG}\n'
              f'PYRO_DMG={self.PYRO_DMG}\n'
              f'CRYO_DMG={self.CRYO_DMG}\n'
              f'HEAL={self.HEAL}\n'
              f'SHIELD={self.SHIELD}\n'
              f'ER={self.ER}')


class Stats:
    def __init__(self):
        self.ATK = []
        self.ATK_p = []
        self.CR = []
        self.CD = []
        self.EM = []
        self.HP = []
        self.HP_p = []
        self.DEF = []
        self.DEF_p = []
        self.PDMG = []
        self.ANEMO_DMG = []
        self.GEO_DMG = []
        self.ELECTRO_DMG = []
        self.HYDRPO_DMG = []
        self.PYRO_DMG = []
        self.CRYO_DMG = []
        self.HEAL = []
        self.SHIELD = []
        self.ER = []


class Character:
    def __init__(self, name, HP, ATK, DEF, CR, CD, ATK_p, EM, HP_p, DEF_p,
                 HEAL, PDMG, EDMG, BSCONDUCT, BOVERLOAD, BELECTROCH, BSWIRL,
                 BSHATTER, BCRYSTALIZE, ER, WEAPON_TYPE, ELEMENTAL, lv):
        self.name = name
        self.HP = HP  # 0
        self.ATK = ATK  # 1
        self.DEF = DEF  # 2
        self.CR = CR  # 3
        self.CD = CD  # 4
        self.ATK_p = ATK_p  # 5
        self.EM = EM  # 6
        self.HP_p = HP_p  # 7
        self.DEF_p = DEF_p  # 8
        self.HEAL = HEAL  # 9
        self.PDMG = PDMG  # 10
        self.EDMG = EDMG  # 11
        self.BSCONDUCT = BSCONDUCT  # 12
        self.BOVERLOAD = BOVERLOAD  # 13
        self.BELECTROCH = BELECTROCH  # 14
        self.BSWIRL = BSWIRL  # 15
        self.BSHATTER = BSHATTER  # 16
        self.BCRYSTALIZE = BCRYSTALIZE  # 17
        self.ER = ER  # 18
        self.WEAPON_TYPE = WEAPON_TYPE  # 19
        self.ELEMENTAL = ELEMENTAL  # 20
        self.level = lv  # 21


class Weapon:
    def __init__(self, ATK, HP_p, ATK_p, DEF_p, CR, CD, EM, ER, PDMG):
        self.ATK = ATK
        self.HP_p = HP_p
        self.ATK_p = ATK_p
        self.DEF_p = DEF_p
        self.CR = CR
        self.CD = CD
        self.EM = EM
        self.ER = ER
        self.PDMG = PDMG


class FinalStats:
    def __init__(self):
        self.atk_normal = 0
        self.atk_average = 0
        self.atk_critical = 0
        self.monster_res = 0
        self.def_normal = 0
        self.def_average = 0
        self.def_critical = 0
        self.hp_normal = 0
        self.hp_average = 0
        self.hp_critical = 0
        self.em = 0
        self.er = 0
        self.overloaded = 0
        self.electrocharged = 0
        self.swirl = 0
        self.shatter = 0
        self.superconduct = 0

app = None

# for setting stats
atk_flat_bonus = 0
atk_percent_bonus = 0
def_flat_bonus = 0
def_percent_bonus = 0
hp_flat_bonus = 0
hp_percent_bonus = 0
cr_bonus = 0
cd_bonus = 0
em_bonus = 0
mon_res = 10
mon_lv = 76
mon_res_debuff = 0
mon_def_debuff = 0
reaction_dmg_bonus = 0
max_hp_dmg_bonus = 0
all_dmg_bonus = 0


# for clear and change GUI
talent_name_label = []
talent_level_combobox = []
sub_talent_label = []
sub_talent_damage_label = []
talent_level_var = []
final_stats = FinalStats()
drew = False

# for save selected data
artifact = [None]*5
selected_character = None
selected_weapon = None
artifact_stat = ArtifactStat()

# for fetch data from xlsx
data_file = openpyxl.open('./data/characters_weapons.xlsx')
weapons_data = None
talent = None

# data for indexing
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
    'Traveler Male Anemo',
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
    'Kujou Sara',
    'Traveler Female Anemo',
    'Traveler Male Geo',
    'Traveler Female Geo',
    'Traveler Male Electro',
    'Traveler Female Electro'
]


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
    load_all_atf()


def load_all_atf():
    global artifact_stat
    artifact_stat = ArtifactStat()
    for each_atf in artifact:
        if each_atf is None:
            continue
        main_stat_name = each_atf['main_stat_name']
        main_stat_value = each_atf['main_stat_value']
        if main_stat_name == 'hp':
            if main_stat_value[1] == 0:
                artifact_stat.HP.append(main_stat_value[0])
            elif main_stat_value[1] == 1:
                artifact_stat.HP_p.append(main_stat_value[0]/100)
        elif main_stat_name == 'atk':
            if main_stat_value[1] == 0:
                artifact_stat.ATK.append(main_stat_value[0])
            elif main_stat_value[1] == 1:
                artifact_stat.ATK_p.append(main_stat_value[0]/100)
        elif main_stat_name == 'def':
            if main_stat_value[1] == 0:
                artifact_stat.DEF.append(main_stat_value[0])
            elif main_stat_value[1] == 1:
                artifact_stat.DEF_p.append(main_stat_value[0]/100)
        elif main_stat_name == 'element':
            artifact_stat.EM.append(main_stat_value[0])
        elif main_stat_name == 'energy':
            artifact_stat.ER.append(main_stat_value[0]/100)
        elif main_stat_name == 'physical':
            artifact_stat.PDMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'anemo':
            artifact_stat.ANEMO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'geo':
            artifact_stat.GEO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'electro':
            artifact_stat.ELECTRO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'hydro':
            artifact_stat.HYDRPO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'pyro':
            artifact_stat.PYRO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'cryo':
            artifact_stat.CRYO_DMG.append(main_stat_value[0]/100)
        elif main_stat_name == 'cri_rate':
            artifact_stat.CR.append(main_stat_value[0]/100)
        elif main_stat_name == 'cri_dmg':
            artifact_stat.CD.append(main_stat_value[0]/100)
        elif main_stat_name == 'healing':
            artifact_stat.HEAL.append(main_stat_value[0]/100)

        sub_stats_name = each_atf['sub_stat_name']
        sub_stats_value = each_atf['sub_stat_value']
        for i, each_sub_name in enumerate(sub_stats_name):
            each_sub_value = sub_stats_value[i]
            if each_sub_name == 'hp':
                if each_sub_value[1] == 0:
                    artifact_stat.HP.append(each_sub_value[0])
                elif each_sub_value[1] == 1:
                    artifact_stat.HP_p.append(each_sub_value[0]/100)
            elif each_sub_name == 'atk':
                if each_sub_value[1] == 0:
                    artifact_stat.ATK.append(each_sub_value[0])
                elif each_sub_value[1] == 1:
                    artifact_stat.ATK_p.append(each_sub_value[0]/100)
            elif each_sub_name == 'def':
                if each_sub_value[1] == 0:
                    artifact_stat.DEF.append(each_sub_value[0])
                elif each_sub_value[1] == 1:
                    artifact_stat.DEF_p.append(each_sub_value[0]/100)
            elif each_sub_name == 'cri_dmg':
                artifact_stat.CD.append(each_sub_value[0]/100)
            elif each_sub_name == 'cri_rate':
                artifact_stat.CR.append(each_sub_value[0]/100)
            elif each_sub_name == 'element':
                artifact_stat.EM.append(each_sub_value[0])
            elif each_sub_name == 'energy':
                artifact_stat.ER.append(each_sub_value[0]/100)

    artifact_stat.print_log()
    # TODO add artifact effect


def load_weapons_data():
    weapons = data_file['Weapons']
    r_count = 0
    row = 2 + (27 * r_count)
    weapons_d = []
    while weapons[f'A{row}'].value is not None:
        weapons_d.append([weapons[f'A{row}'].value, weapons[f'B{row}'].value, weapons[f'C{row}'].value, row])
        r_count += 1
        row = 2 + (27 * r_count)
    return weapons_d  # (weapon name, type, rarity, row of data)


def get_character_info(char_name, level):
    characters = data_file['Characters']
    row = 2 + (character_name.index(char_name)*16) + char_level_offset.index(level)
    stats = []
    stat_offset = [
        'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'H'
    ]
    for each_stat in stat_offset:
        if each_stat in ['P', 'Q', 'R', 'S', 'T', 'U']:
            value = characters[f'{each_stat}{2 + char_level_offset.index(level)}'].value
        elif each_stat == 'X' or each_stat == 'Y':
            value = characters[f'X{2 + (character_name.index(char_name)*16)}'].value
        else:
            value = characters[f'{each_stat}{row}'].value
        if value is None:
            value = 0
        stats.append(value)
    return Character(char_name, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6],
                     stats[7], stats[8], stats[9], stats[10], stats[11], stats[12], stats[13],
                     stats[14], stats[15], stats[16], stats[17], stats[18], stats[19], stats[20], stats[21])


def get_weapon_info(weapon_name, weapon_level):
    weapons = data_file['Weapons']
    global weapons_data
    row = list(weapons_data[i][3] for i, each_weapon_data in enumerate(weapons_data) if each_weapon_data[0] == weapon_name)[0]
    row = int(row) + weapons_level_offset.index(weapon_level)
    weapon_stat_column = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    weapon_d = []
    for each_column in weapon_stat_column:
        value = weapons[f'{each_column}{row}'].value
        if value is None:
            value = 0
        if each_column not in ['E', 'K']:
            value = value/100
        weapon_d.append(value)
    return Weapon(weapon_d[0], weapon_d[1], weapon_d[2], weapon_d[3], weapon_d[4], weapon_d[5], weapon_d[6], weapon_d[7],
                  weapon_d[8])


def calculate_stats():
    global final_stats
    final_stats = FinalStats()
    if artifact_stat is None or selected_weapon is None or selected_character is None:
        return

    all_cr = selected_character.CR + selected_weapon.CR + sum(artifact_stat.CR) + cr_bonus
    if all_cr > 1:
        all_cr = 1
    all_cd = selected_character.CD + selected_weapon.CD + sum(artifact_stat.CD) + cd_bonus
    # atk_normal_final = (sum_of_Flat_ATK+Char_ATK+Flat_ATK_bonus) + ( ( (sum_of_%_ATK+Char_%_ATK)+ATK_%_bonus) * (Char_ATK+Weapon_ATK) )
    final_stats.atk_normal = (selected_character.ATK + selected_weapon.ATK + sum(artifact_stat.ATK) + atk_flat_bonus) + \
                       (((selected_character.ATK_p + selected_weapon.ATK_p + sum(artifact_stat.ATK_p)) + atk_percent_bonus) * (selected_character.ATK + selected_weapon.ATK))
    # atk_average_final = ATK_normal_final *  (1+(IF((sum_of_CR+ char_cr + cr_bonus)>1 , 1 , (SUM($E$6:$L$6)+$L$65+O11)  )*(sum_of_CD+ char_CD + cd_bonus)))

    final_stats.atk_average = final_stats.atk_normal * (1+(all_cr * all_cd))
    final_stats.atk_critical = final_stats.atk_normal * (1+all_cd)

    final_stats.def_normal = (selected_character.DEF + sum(artifact_stat.DEF) + def_flat_bonus) + \
                       (((selected_character.DEF_p + selected_weapon.DEF_p + sum(
                           artifact_stat.DEF_p)) + def_percent_bonus) * selected_character.DEF)
    final_stats.def_average = final_stats.def_normal * (1+(all_cr * all_cd))
    final_stats.def_critical = final_stats.def_normal * (1+all_cd)

    final_stats.hp_normal = (selected_character.HP + sum(artifact_stat.HP) + hp_flat_bonus) + \
                       (((selected_character.HP_p + selected_weapon.HP_p + sum(
                           artifact_stat.HP_p)) + hp_percent_bonus) * selected_character.HP)
    final_stats.hp_average = final_stats.hp_normal * (1 + (all_cr * all_cd))
    final_stats.hp_critical = final_stats.hp_normal * (1 + all_cd)

    final_stats.em = selected_character.EM + selected_weapon.EM + sum(artifact_stat.EM) + em_bonus

    final_stats.er = 1 + selected_character.ER + selected_weapon.ER + sum(artifact_stat.ER)

    if mon_res_debuff < 0:
        final_stats.monster_res = mon_res + mon_res_debuff*100 - \
                            ((mon_res + mon_res_debuff * 100)/2 if (mon_res + mon_res_debuff * 100) < 0 else 0)
    else:
        A = (mon_res_debuff * 100 if mon_res_debuff > 0 else 0)
        B = ((mon_res - A) / 2 if (mon_res - A) < 0 else 0)
        final_stats.monster_res = mon_res - A - B

    final_stats.overloaded = selected_character.BOVERLOAD * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + reaction_dmg_bonus)

    final_stats.electrocharged = selected_character.BELECTROCH * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + reaction_dmg_bonus)

    final_stats.swirl = selected_character.BSWIRL * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + reaction_dmg_bonus)

    final_stats.shatter = selected_character.BSHATTER * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + reaction_dmg_bonus)

    final_stats.superconduct = selected_character.BSCONDUCT * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + reaction_dmg_bonus)

    # print(f'ATK normal final: {final_stats.atk_normal}\n'
    #       f'ATK average final: {final_stats.atk_average}\n'
    #       f'ATK critical final: {final_stats.atk_critical}')
    # print(f'Monster RES final: {final_stats.monster_res}')
    # print(f'DEF normal final: {final_stats.def_normal}\n'
    #       f'DEF average final: {final_stats.def_average}\n'
    #       f'DEF critical final: {final_stats.def_critical}')
    # print(f'HP normal final: {final_stats.hp_normal}\n'
    #       f'HP average final: {final_stats.hp_average}\n'
    #       f'HP critical final: {final_stats.hp_critical}')
    # print(f'Elemental Mastery final: {final_stats.em}')
    # print(f'Energy Recharge final: {final_stats.er}')
    # print(f'overloaded: {final_stats.overloaded}\n'
    #       f'electrocharged: {final_stats.electrocharged}\n'
    #       f'swirl: {final_stats.swirl}\n'
    #       f'shatter: {final_stats.shatter}\n'
    #       f'superconduct: {final_stats.superconduct}')


def load_talent():
    atk_talent_file = openpyxl.open('./data/attack_talents.xlsx')
    if selected_character is None:
        return None
    atk_talent = atk_talent_file[selected_character.name]
    line = 1
    global talent
    talent = []
    talent_level_column = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    while True:
        A = atk_talent[f'A{line}'].value
        if A is not None:
            talent.append([A, []])
            line += 1
            while True:
                B = atk_talent[f'B{line}'].value
                percent = []
                for each_column in talent_level_column:
                    percent.append(atk_talent[f'{each_column}{line}'].value)
                if B is not None:
                    talent[len(talent)-1][1].append((B, percent))
                else:
                    break
                line += 1
        else:
            break


def set_alpha(value):
    app.attributes('-alpha', float(value) / 100)
    app.update()


# draw stats window
def draw_window():

    def row(r):
        return 10 + (r*30)

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
        load_talent()
        weapon_name_changed(self)

    character_label = tk.Label(app)
    character_label.place(x=10, y=10, height=24)
    character_label.configure(text='Character')
    set_color(character_label)

    char_name_choices = sorted(character_name)
    char_name_var = tk.StringVar(app)
    char_name_var.set(char_name_choices[0])
    char_name_dropdown = ttk.Combobox(app, textvariable=char_name_var, values=char_name_choices)
    char_name_dropdown.bind('<<ComboboxSelected>>', character_change)
    char_name_dropdown.place(x=70, y=row(0), width=150, height=24)

    char_level_choices = char_level_offset
    char_level_var = tk.StringVar(app)
    char_level_var.set(char_level_offset[len(char_level_offset) - 1])
    char_level_dropdown = ttk.Combobox(app, textvariable=char_level_var, values=char_level_choices)
    char_level_dropdown.bind('<<ComboboxSelected>>', character_change)
    char_level_dropdown.place(x=230, y=row(0), width=60, height=24)

    def weapon_name_changed(self):
        global selected_weapon
        selected_weapon = get_weapon_info(weapon_name_var.get(), weapon_level_var.get())
        rarity = [weapons_data[i][2] for i, _ in enumerate(weapons_data) if weapons_data[i][0] == weapon_name_var.get()]
        if len(rarity) > 0 and (rarity[0] == 1 or rarity[0] == 2):
            weapons_level = weapons_level_offset[0:19]
            if weapon_level_var.get() not in weapons_level:
                weapon_level_var.set(weapons_level[len(weapons_level)-1])
        else:
            weapons_level = weapons_level_offset
        weapon_level_dropdown.config(value=weapons_level)
        draw_talent()

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
    weapon_name_dropdown.place(x=70, y=row(1), width=150, height=24)

    weapon_level_choices = weapons_level_offset
    weapon_level_var = tk.StringVar(app)
    weapon_level_var.set(weapons_level_offset[len(weapons_level_offset) - 1])
    weapon_level_dropdown = ttk.Combobox(app, textvariable=weapon_level_var, values=weapon_level_choices)
    weapon_level_dropdown.bind('<<ComboboxSelected>>', weapon_name_changed)
    weapon_level_dropdown.place(x=230, y=row(1), width=60, height=24)

    def calcurate_talent_dmg(talent_value, talent_type):
        talent_value_add = 0
        talent_value_multi = 1
        dmg_base = final_stats.atk_normal

        if talent_type in ['e', 'p']:
            talent_value = talent_value.split('+')
            if len(talent_value) >= 2:
                talent_value_add = int(talent_value[1])
            talent_value = talent_value[0].split('|')
            if len(talent_value) >= 2:
                if talent_value[1] == 'DEF':
                    dmg_base = final_stats.def_normal
                elif talent_value[1] == 'Max HP':
                    dmg_base = final_stats.hp_normal
                else:
                    print(f'dmg_base error: {talent_value[1]}')
            talent_value = talent_value[0].split('*')
            if len(talent_value) >= 2:
                talent_value_multi = int(talent_value[1])
            talent_value = talent_value[0].split('&')
            return_value = []
            for each_value in talent_value:
                return_value.append(float(each_value[0:len(each_value) - 1]))
            talent_value = return_value

            if talent_type == 'p':
                pe_dmg_bonus = selected_character.PDMG + sum(artifact_stat.PDMG)
            elif talent_type == 'e':
                pe_dmg_bonus = selected_character.EDMG
                if selected_character.ELEMENTAL == 'Anemo':
                    pe_dmg_bonus += sum(artifact_stat.ANEMO_DMG)
                elif selected_character.ELEMENTAL == 'Geo':
                    pe_dmg_bonus += sum(artifact_stat.GEO_DMG)
                elif selected_character.ELEMENTAL == 'Electro':
                    pe_dmg_bonus += sum(artifact_stat.ELECTRO_DMG)
                elif selected_character.ELEMENTAL == 'Hydro':
                    pe_dmg_bonus += sum(artifact_stat.HYDRPO_DMG_DMG)
                elif selected_character.ELEMENTAL == 'Pyro':
                    pe_dmg_bonus += sum(artifact_stat.PYRO_DMG_DMG)
                elif selected_character.ELEMENTAL == 'Cryo':
                    pe_dmg_bonus += sum(artifact_stat.CRYO_DMG_DMG)
            a = ((100 + selected_character.level) / ((100 + selected_character.level) + ((100 + mon_lv) * (1 + mon_def_debuff))))
            b = ((max_hp_dmg_bonus * final_stats.hp_normal) * (1 - final_stats.monster_res / 100) * (
                        (100 + selected_character.level) / ((100 + selected_character.level) + (100 + mon_lv))))
            temp_value = []
            for each_value in talent_value:
                temp_value.append((dmg_base * (1- final_stats.monster_res/100)* a * (each_value/100) + b) * 1 * (1+ all_dmg_bonus + pe_dmg_bonus))
            talent_value_final = ''
            for i, each_temp in enumerate(temp_value):
                talent_value_final += str(round(each_temp))
                if i+1 < len(temp_value):
                    talent_value_final += ' + '
        else:
            talent_value_final = str(talent_value)

        return talent_value_final

    def draw_talent():
        calculate_stats()
        global talent_name_label, sub_talent_label, talent_level_var
        for each_main in talent_name_label:
            each_main.destroy()
        for each_sub in sub_talent_label:
            each_sub.destroy()
        for each_sub_dmg in sub_talent_damage_label:
            each_sub_dmg.destroy()
        current_row = 3

        for i, each_talent in enumerate(talent):
            current_row += 1
            # draw talent name
            talent_name_label.append(tk.Label(app))
            last_talent_name_label = len(talent_name_label)-1
            talent_name_label[last_talent_name_label].place(x=20, y=row(current_row), height=24)
            talent_name_label[last_talent_name_label].configure(text=each_talent[0])
            set_color(talent_name_label[last_talent_name_label])

            talent_level_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            if len(talent_level_var) > i:
                pass
            else:
                talent_level_var.append(tk.StringVar(app))
                talent_level_var[len(talent_level_var)-1].set(talent_level_choices[9])
            talent_level_combobox.append(ttk.Combobox(app, textvariable=talent_level_var[i], values=talent_level_choices))
            last_talent_level_combobox = len(talent_level_combobox) - 1
            talent_level_combobox[last_talent_level_combobox].bind('<<ComboboxSelected>>', character_change)
            talent_level_combobox[last_talent_level_combobox].place(x=270, y=row(current_row), width=60, height=24)

            level = int(talent_level_var[i].get()) - 1

            for each_sub in each_talent[1]:
                # draw talent's sub name
                current_row += 1
                sub_talent_label.append(tk.Label(app))
                last_sub_talent_label = len(sub_talent_label)-1
                sub_talent_label[last_sub_talent_label].place(x=40, y=row(current_row), height=24)
                sub_talent_label[last_sub_talent_label].configure(text=f'- {each_sub[0]}')
                set_color(sub_talent_label[last_sub_talent_label])

                # calculate talent's sub damage
                talent_value = calcurate_talent_dmg(each_sub[1][level], each_sub[1][15])

                # draw talent's sub damage
                sub_talent_damage_label.append(tk.Label(app))
                last_sub_talent_damage_label = len(sub_talent_damage_label)-1
                sub_talent_damage_label[last_sub_talent_damage_label].place(x=230, y=row(current_row), width=100, height=24)
                sub_talent_damage_label[last_sub_talent_damage_label].configure(text=talent_value, anchor='e', justify=tk.RIGHT)
                set_color(sub_talent_damage_label[last_sub_talent_damage_label])
        global drew
        if not drew:
            app.geometry(f'350x{row(current_row + 1) + 6}+140+10')
            drew = True
        else:
            app.geometry(f'350x{row(current_row + 1) + 6}+{app.winfo_x()}+{app.winfo_y()}')

    # refresh weapon name and talent
    character_change(None)

    talent_label = tk.Label(app)
    talent_label.place(x=10, y=row(3), height=24)
    talent_label.configure(text='Talent Damage', font=('TkDefaultFont', 12))
    set_color(talent_label)

    app.attributes('-topmost', True)
    app.attributes('-alpha', 0.95)
    app.mainloop()


def main():
    global weapons_data
    weapons_data = load_weapons_data()
    load_all_atf()
    draw_window()