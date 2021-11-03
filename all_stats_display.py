import os

import openpyxl
import tkinter as tk
from tkinter import ttk
import pickle

from class_file.artifact_stat import ArtifactStat
from class_file.stats import Stats
from class_file.character import Character
from class_file.weapon import Weapon
from class_file.filnal_stats import FinalStats
from class_file.app import AppTopLevel
from class_file.tooltip import create_tool_tip

from function.set_widget_color import set_color, bg_color, fg_color
from function.stat_update import update_stat
import stats_confirm
from main import app

all_stats_display_app = None
toggle = True

# for setting stats
stats = Stats()
option_stats = Stats()
stats_sum = Stats()
# atk_flat_bonus = 0
# atk_percent_bonus = 0
# def_flat_bonus = 0
# def_percent_bonus = 0
# hp_flat_bonus = 0
# hp_percent_bonus = 0
# cr_bonus = 0
# cd_bonus = 0
# em_bonus = 0
mon_res = 10
mon_lv = 76
# mon_res_debuff = 0
# mon_def_debuff = 0
# reaction_dmg_bonus = 0
# max_hp_dmg_bonus = 0
# all_dmg_bonus = 0


# for clear and change GUI
talent_name_label = []
talent_level_combobox = []
sub_talent_label = []
sub_talent_damage_label = []
talent_level_var = []
final_stats = FinalStats()
drew = False
alpha = 95
atf_btn = [None]*5

# for save selected data
artifacts = [None] * 5
selected_character = None
selected_weapon = None
artifact_stat = ArtifactStat()
save_data = None

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


def write_save(obj):
    with open('data/save.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    print('saved')


def read_save():
    if os.path.isfile('data/save.pkl'):
        with open('data/save.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return {'characters': {}}


def refresh_atf_btn():
    global artifacts
    for i in range(5):
        if artifacts[i] is not None:
            atf_btn[i].configure(state='normal')
        else:
            atf_btn[i].configure(state='disabled')


def change_atf(atf_data):
    global artifacts
    part_name = atf_data['part_name']
    atf_data['owner'] = selected_character.name
    if part_name == 'flower':
        artifacts[0] = atf_data
    elif part_name == 'plume':
        artifacts[1] = atf_data
    elif part_name == 'sands':
        artifacts[2] = atf_data
    elif part_name == 'goblet':
        artifacts[3] = atf_data
    elif part_name == 'circlet':
        artifacts[4] = atf_data
    else:
        print(f'change atf error. part name not match ({part_name})')
    global save_data
    save_data['characters'][selected_character.name]['artifacts'] = artifacts
    write_save(save_data)
    load_all_atf()
    refresh_atf_btn()


def remove_atf(part_name, owner):
    global artifacts
    if part_name == 'flower':
        artifacts[0] = None
    elif part_name == 'plume':
        artifacts[1] = None
    elif part_name == 'sands':
        artifacts[2] = None
    elif part_name == 'goblet':
        artifacts[3] = None
    elif part_name == 'circlet':
        artifacts[4] = None
    global save_data
    save_data['characters'][owner]['artifacts'] = artifacts
    write_save(save_data)
    load_all_atf()
    refresh_atf_btn()


def load_all_atf():
    global artifact_stat
    artifact_stat = ArtifactStat()
    for each_atf in artifacts:
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
            artifact_stat.HYDRO_DMG.append(main_stat_value[0]/100)
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
    draw_talent()
    # artifact_stat.print_log()
    # TODO add artifacts effect


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
    char_row = 2 + (character_name.index(char_name)*16) + char_level_offset.index(level)
    char_stats = []
    stat_offset = [
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y'
    ]
    for each_stat in stat_offset:
        if each_stat in ['P', 'Q', 'R', 'S', 'T', 'U']:
            value = characters[f'{each_stat}{2 + char_level_offset.index(level)}'].value
        elif each_stat == 'X' or each_stat == 'Y':
            value = characters[f'{each_stat}{2 + (character_name.index(char_name)*16)}'].value
        else:
            value = characters[f'{each_stat}{char_row}'].value
        if value is None:
            value = 0
        char_stats.append(value)
    return Character(char_name, char_stats[0], char_stats[1], char_stats[2], char_stats[3], char_stats[4], char_stats[5], char_stats[6],
                     char_stats[7], char_stats[8], char_stats[9], char_stats[10], char_stats[11], char_stats[12], char_stats[13],
                     char_stats[14], char_stats[15], char_stats[16], char_stats[17], char_stats[18], char_stats[19], char_stats[20], char_stats[21])


def get_weapon_info(weapon_name, weapon_level):
    weapons = data_file['Weapons']
    global weapons_data
    weapon_row = list(weapons_data[i][3] for i, each_weapon_data in enumerate(weapons_data) if each_weapon_data[0] == weapon_name)[0]
    weapon_row = int(weapon_row) + weapons_level_offset.index(weapon_level)
    weapon_stat_column = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    weapon_d = []
    for each_column in weapon_stat_column:
        value = weapons[f'{each_column}{weapon_row}'].value
        if value is None:
            value = 0
        if each_column not in ['E', 'K']:
            value = value/100
        weapon_d.append(value)
    return Weapon(weapon_name, weapon_d[0], weapon_d[1], weapon_d[2], weapon_d[3], weapon_d[4], weapon_d[5], weapon_d[6], weapon_d[7],
                  weapon_d[8])


def calculate_stats():
    global final_stats
    final_stats = FinalStats()
    if artifact_stat is None or selected_weapon is None or selected_character is None:
        print('calcurate_stats_return')
        return

    global stats, option_stats, stats_sum
    stats_sum = stats + option_stats

    all_cr = selected_character.CR + selected_weapon.CR + sum(artifact_stat.CR) + stats_sum.CR
    if all_cr > 1:
        all_cr = 1
    all_cd = selected_character.CD + selected_weapon.CD + sum(artifact_stat.CD) + stats_sum.CD

    final_stats.def_normal = (selected_character.DEF + sum(artifact_stat.DEF) + stats_sum.DEF) + \
                       (((selected_character.DEF_p + selected_weapon.DEF_p + sum(
                           artifact_stat.DEF_p)) + stats_sum.DEF_p) * selected_character.DEF)
    final_stats.def_average = final_stats.def_normal * (1+(all_cr * all_cd))
    final_stats.def_critical = final_stats.def_normal * (1+all_cd)

    final_stats.hp_normal = (selected_character.HP + sum(artifact_stat.HP) + stats_sum.HP) + \
                       (((selected_character.HP_p + selected_weapon.HP_p + sum(artifact_stat.HP_p)) +
                         stats_sum.HP_p) * selected_character.HP)
    final_stats.hp_average = final_stats.hp_normal * (1 + (all_cr * all_cd))
    final_stats.hp_critical = final_stats.hp_normal * (1 + all_cd)

    # atk_normal_final = (sum_of_Flat_ATK+Char_ATK+Flat_ATK_bonus) + ( ( (sum_of_%_ATK+Char_%_ATK)+ATK_%_bonus) * (Char_ATK+Weapon_ATK) )
    final_stats.atk_normal = (selected_character.ATK + selected_weapon.ATK + sum(artifact_stat.ATK) + stats_sum.ATK) + \
                             (((selected_character.ATK_p + selected_weapon.ATK_p + sum(
                                 artifact_stat.ATK_p)) + stats_sum.ATK_p) * (
                                          selected_character.ATK + selected_weapon.ATK)) + (stats_sum.max_hp_atk_bonus * final_stats.hp_normal)
    # atk_average_final = ATK_normal_final *  (1+(IF((sum_of_CR+ char_cr + cr_bonus)>1 , 1 , (SUM($E$6:$L$6)+$L$65+O11)  )*(sum_of_CD+ char_CD + cd_bonus)))

    final_stats.atk_average = final_stats.atk_normal * (1 + (all_cr * all_cd))
    final_stats.atk_critical = final_stats.atk_normal * (1 + all_cd)

    final_stats.em = selected_character.EM + selected_weapon.EM + sum(artifact_stat.EM) + stats_sum.EM

    final_stats.er = 1 + selected_character.ER + selected_weapon.ER + sum(artifact_stat.ER)

    if stats_sum.mon_res_debuff < 0:
        final_stats.monster_res = mon_res + stats_sum.mon_res_debuff*100 - \
                            ((mon_res + stats_sum.mon_res_debuff * 100)/2 if (mon_res + stats_sum.mon_res_debuff * 100) < 0 else 0)
    else:
        A = (stats_sum.mon_res_debuff * 100 if stats_sum.mon_res_debuff > 0 else 0)
        B = ((mon_res - A) / 2 if (mon_res - A) < 0 else 0)
        final_stats.monster_res = mon_res - A - B

    final_stats.overloaded = selected_character.BOVERLOAD * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + stats_sum.reaction_dmg_bonus)

    final_stats.electrocharged = selected_character.BELECTROCH * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + stats_sum.reaction_dmg_bonus)

    final_stats.swirl = selected_character.BSWIRL * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + stats_sum.reaction_dmg_bonus)

    final_stats.shatter = selected_character.BSHATTER * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + stats_sum.reaction_dmg_bonus)

    final_stats.superconduct = selected_character.BSCONDUCT * \
                 (1-mon_res/100) * \
                 (1 + ((1600 * final_stats.em / (2000 + final_stats.em)) / 100) + stats_sum.reaction_dmg_bonus)

    print(f'ATK normal final: {final_stats.atk_normal}\n'
          f'ATK average final: {final_stats.atk_average}\n'
          f'ATK critical final: {final_stats.atk_critical}')
    print(f'Monster RES final: {final_stats.monster_res}')
    print(f'DEF normal final: {final_stats.def_normal}\n'
          f'DEF average final: {final_stats.def_average}\n'
          f'DEF critical final: {final_stats.def_critical}')
    print(f'HP normal final: {final_stats.hp_normal}\n'
          f'HP average final: {final_stats.hp_average}\n'
          f'HP critical final: {final_stats.hp_critical}')
    print(f'Elemental Mastery final: {final_stats.em}')
    print(f'Energy Recharge final: {final_stats.er}')
    print(f'overloaded: {final_stats.overloaded}\n'
          f'electrocharged: {final_stats.electrocharged}\n'
          f'swirl: {final_stats.swirl}\n'
          f'shatter: {final_stats.shatter}\n'
          f'superconduct: {final_stats.superconduct}')


def load_talent():
    atk_talent_file = openpyxl.open('./data/attack_talents.xlsx')
    if selected_character is None:
        return None
    atk_talent = atk_talent_file[selected_character.name]
    line = 1
    global talent
    talent = []
    talent_level_column = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
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


def calculate_talent_dmg(talent_value, talent_type, normal_atk_type, talent_index):
    talent_value_add = 0
    talent_value_multi = 1
    dmg_base = final_stats.atk_normal
    dmg_base_crit = final_stats.atk_critical
    dmg_base_average = final_stats.atk_average

    if talent_type in ['e', 'p', 'h', None]:
        talent_value = talent_value.split('+')
        if len(talent_value) >= 2:
            talent_value_add = int(talent_value[1])
        talent_value = talent_value[0].split('|')
        if len(talent_value) >= 2:
            if talent_value[1] == 'DEF':
                dmg_base = final_stats.def_normal
                dmg_base_crit = final_stats.def_critical
                dmg_base_average = final_stats.def_average
            elif talent_value[1] == 'Max HP':
                dmg_base = final_stats.hp_normal
                dmg_base_crit = final_stats.hp_critical
                dmg_base_average = final_stats.hp_average
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

        pe_dmg_bonus = 0
        if talent_type == 'p':
            pe_dmg_bonus = selected_character.PDMG + sum(artifact_stat.PDMG)
        elif talent_type == 'e' or talent_index in [1, 2]:
            pe_dmg_bonus = selected_character.EDMG
            pe_dmg_bonus += stats_sum.EDMG
            # check character elemental and and element dmg that match with them
            if selected_character.ELEMENTAL == 'Anemo':
                pe_dmg_bonus += sum(artifact_stat.ANEMO_DMG)
                pe_dmg_bonus += stats_sum.ANEMO_DMG
            elif selected_character.ELEMENTAL == 'Geo':
                pe_dmg_bonus += sum(artifact_stat.GEO_DMG)
                pe_dmg_bonus += stats_sum.GEO_DMG
            elif selected_character.ELEMENTAL == 'Electro':
                pe_dmg_bonus += sum(artifact_stat.ELECTRO_DMG)
                pe_dmg_bonus += stats_sum.ELECTRO_DMG
            elif selected_character.ELEMENTAL == 'Hydro':
                pe_dmg_bonus += sum(artifact_stat.HYDRO_DMG)
                pe_dmg_bonus += stats_sum.HYDRO_DMG
            elif selected_character.ELEMENTAL == 'Pyro':
                pe_dmg_bonus += sum(artifact_stat.PYRO_DMG)
                pe_dmg_bonus += stats_sum.PYRO_DMG
            elif selected_character.ELEMENTAL == 'Cryo':
                pe_dmg_bonus += sum(artifact_stat.CRYO_DMG)
                pe_dmg_bonus += stats_sum.CRYO_DMG

        all_dmg_bonus = stats_sum.all_dmg_bonus
        if talent_index == 0:
            if normal_atk_type == 'n':
                all_dmg_bonus += stats_sum.normal_attack_dmg_bonus
            if normal_atk_type == 'c':
                all_dmg_bonus += stats_sum.charge_attack_dmg_bonus
            if normal_atk_type == 'p':
                all_dmg_bonus += stats_sum.plunging_attack_dmg_bonus
        elif talent_index == 1:
            all_dmg_bonus += stats_sum.element_skill_dmg_bonus
        elif talent_index == 2:
            all_dmg_bonus += stats_sum.element_burst_dmg_bonus

        a = ((100 + selected_character.level) / ((100 + selected_character.level) + ((100 + mon_lv) * (1 + stats_sum.mon_def_debuff))))
        b = ((stats_sum.max_hp_dmg_bonus * final_stats.hp_normal) * (1 - final_stats.monster_res / 100) * (
                    (100 + selected_character.level) / ((100 + selected_character.level) + (100 + mon_lv))))
        temp_value = []
        temp_crit_value = []
        temp_average_value = []
        for each_value in talent_value:
            temp_value.append((dmg_base * (1- final_stats.monster_res/100)* a * (each_value/100) + b) * 1 * (1+ all_dmg_bonus + pe_dmg_bonus))
            temp_crit_value.append((dmg_base_crit * (1 - final_stats.monster_res / 100) * a * (each_value / 100) + b) * 1 * (
                        1 + all_dmg_bonus + pe_dmg_bonus))
            temp_average_value.append((dmg_base_average * (1 - final_stats.monster_res / 100) * a * (each_value / 100) + b) * 1 * (
                        1 + all_dmg_bonus + pe_dmg_bonus))

        talent_value_final = [None]*3
        for i, each_temp in enumerate(temp_value):
            talent_value_final[0] = ''
            talent_value_final[0] += str(round(each_temp) + (int(talent_value_add) if talent_value_add else 0))
            if i+1 < len(temp_value):
                talent_value_final[0] += ' + '
            if talent_value_multi > 1:
                talent_value_final[0] += f'*{talent_value_multi}'
        for i, each_temp in enumerate(temp_crit_value):
            talent_value_final[1] = ''
            talent_value_final[1] += str(round(each_temp) + (int(talent_value_add) if talent_value_add else 0))
            if i+1 < len(temp_value):
                talent_value_final[1] += ' + '
            if talent_value_multi > 1:
                talent_value_final[1] += f'*{talent_value_multi}'
        for i, each_temp in enumerate(temp_average_value):
            talent_value_final[2] = ''
            talent_value_final[2] += str(round(each_temp) + (int(talent_value_add) if talent_value_add else 0))
            if i+1 < len(temp_value):
                talent_value_final[2] += ' + '
            if talent_value_multi > 1:
                talent_value_final[2] += f'*{talent_value_multi}'
    elif talent_type in ['n_bonus']:
        # TODO make n_bonus works
        talent_value_final = 'under_dev'
    else:
        talent_value_final = [None]*3
        talent_value_final[0] = str(talent_value)
        talent_value_final[1] = str(talent_value)
        talent_value_final[2] = str(talent_value)

    return talent_value_final


def row(r):
    return 40 + (r*30)


def set_alpha(value):
    all_stats_display_app.attributes('-alpha', float(value) / 100)
    all_stats_display_app.update()
    global alpha
    alpha = value


def toggle_show():
    global all_stats_display_app, toggle
    if toggle:
        all_stats_display_app.withdraw()
        toggle = False
    else:
        all_stats_display_app.deiconify()
        toggle = True


def draw_talent(stats_update=True):
    global talent_name_label, sub_talent_label, talent_level_var, talent_level_combobox

    def talent_change(event, i):
        save_data['characters'][selected_character.name]['talents_level'][i] = talent_level_var[i].get()
        write_save(save_data)
        draw_talent()
    if selected_character and selected_weapon:
        if stats_update:
            global stats
            stats = update_stat(selected_character, selected_weapon, artifacts, stats)
        calculate_stats()

    for each_main in talent_name_label:
        each_main.destroy()
    for each_sub in sub_talent_label:
        each_sub.destroy()
    for each_sub_dmg in sub_talent_damage_label:
        each_sub_dmg.destroy()
    for each_combobox in talent_level_combobox:
        each_combobox.destroy()
    current_row = 4

    if talent is None:
        return
    talent_level_var.clear()
    for i, each_talent in enumerate(talent):
        current_row += 1
        # draw talent name
        talent_name_label.append(tk.Label(all_stats_display_app))
        last_talent_name_label = len(talent_name_label)-1
        talent_name_label[last_talent_name_label].place(x=10, y=row(current_row), height=24)
        talent_name_label[last_talent_name_label].configure(text=each_talent[0])
        set_color(talent_name_label[last_talent_name_label])

        talent_level_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        talent_level_var.append(tk.StringVar(all_stats_display_app))
        if selected_character.name in save_data['characters'] and len(save_data['characters'][selected_character.name]['talents_level']) > 0:
            talent_level_var[i].set(save_data['characters'][selected_character.name]['talents_level'][i])
        else:
            talent_level_var[i].set(talent_level_choices[9])
        talent_level_combobox.append(ttk.Combobox(all_stats_display_app, textvariable=talent_level_var[i], values=talent_level_choices))
        last_talent_level_combobox = len(talent_level_combobox) - 1
        talent_level_combobox[last_talent_level_combobox].bind('<<ComboboxSelected>>', lambda event, talent_i=i: talent_change(event, talent_i))
        talent_level_combobox[last_talent_level_combobox].place(x=276, y=row(current_row), width=60, height=24)

        level = int(talent_level_var[i].get()) - 1

        for each_sub in each_talent[1]:
            # draw talent's sub name
            current_row += 1
            sub_talent_label.append(tk.Label(all_stats_display_app))
            last_sub_talent_label = len(sub_talent_label)-1
            sub_talent_label[last_sub_talent_label].place(x=20, y=row(current_row), height=24)
            sub_talent_label[last_sub_talent_label].configure(text=f'- {each_sub[0]}')
            set_color(sub_talent_label[last_sub_talent_label])

            # calculate talent's sub damage
            talent_value = calculate_talent_dmg(each_sub[1][level], each_sub[1][15], each_sub[1][16], i)

            # draw talent's sub damage
            sub_talent_damage_label.append(tk.Label(all_stats_display_app))
            last_sub_talent_damage_label = len(sub_talent_damage_label)-1
            sub_talent_damage_label[last_sub_talent_damage_label].place(x=188, y=row(current_row), width=150, height=24)
            sub_talent_damage_label[last_sub_talent_damage_label].configure(text=' | '.join(talent_value), anchor='e', justify=tk.RIGHT)
            set_color(sub_talent_damage_label[last_sub_talent_damage_label])
            create_tool_tip(sub_talent_damage_label[last_sub_talent_damage_label], text=f'normal dmg: {talent_value[0]} | critical dmg: {talent_value[1]} | average dmg: {talent_value[2]}')
    global drew
    if not drew:
        all_stats_display_app.geometry(f'350x{row(current_row + 1) + 6}+140+10')
        drew = True
    else:
        # all_stats_display_app.geometry(f'350x{row(current_row + 1) + 6}+{all_stats_display_app.winfo_x()}+{all_stats_display_app.winfo_y()}')
        all_stats_display_app.geometry(f'350x{row(current_row + 1) + 6}')


# draw stats window
def draw_window():
    global save_data, weapons_data

    global all_stats_display_app
    all_stats_display_app = AppTopLevel(app)

    head_canvas = tk.Canvas(all_stats_display_app)
    head_canvas.configure(width=350, height=25, bd=0, bg='#111199', highlightthickness=0)
    head_canvas.place(x=0, y=0)
    all_stats_display_app.update()

    all_stats_display_app.configure(bg=bg_color)
    all_stats_display_app.option_add("*TCombobox*Listbox*Background", bg_color)
    all_stats_display_app.option_add("*TCombobox*Listbox*Foreground", fg_color)

    # save selected data to file
    def save_selected_data():
        selected_character_name = save_data['selected_character']
        if selected_character_name not in save_data['characters']:
            save_data['characters'][selected_character_name] = None
        save_data['characters'][selected_character_name] = {'level': char_level_var.get(),
                                                            'weapon': weapon_name_var.get(),
                                                            'weapon_level': weapon_level_var.get(),
                                                            'artifacts': artifacts.copy(),
                                                            'talents_level': []}
        if 'mon_res' not in save_data:
            save_data['mon_res'] = mon_res
            save_data['mon_lv'] = mon_lv
        for each_talent_level in talent_level_var:
            save_data['characters'][selected_character_name]['talents_level'].append(each_talent_level.get())
        write_save(save_data)

    # when change character,
    # 1. load character level
    # 2. change weapon_name ComboBox
    def character_change(self):

        global selected_character
        selected_character = get_character_info(char_name_var.get(), char_level_var.get())

        # change the character level's ComboBox if save is found
        if char_name_var.get() in save_data['characters']:
            char_level_var.set(save_data['characters'][char_name_var.get()]['level'])

        # change weapon name ComboBox's value
        _weapons_name = sorted([weapons_data[i][0] for i, _ in enumerate(weapons_data) if weapons_data[i][1] == selected_character.WEAPON_TYPE])
        if char_name_var.get() in save_data['characters']:
            weapon_name_var.set(save_data['characters'][char_name_var.get()]['weapon'])
        elif weapon_name_var.get() not in _weapons_name and len(_weapons_name) > 0:
            weapon_name_var.set(_weapons_name[0])
        weapon_name_combobox.config(value=_weapons_name)

        # load character's artifacts save
        global artifacts
        if char_name_var.get() in save_data['characters']:
            artifacts = save_data['characters'][char_name_var.get()]['artifacts'].copy()
            refresh_atf_btn()
        else:
            artifacts = [None] * 5
            refresh_atf_btn()
        load_all_atf()

        # change selected character
        selected_character = get_character_info(char_name_var.get(), char_level_var.get())
        save_data['selected_character'] = char_name_var.get()

        # load talent of selected character
        load_talent()

        # refresh weapon ComboBox and it's value to match with character
        weapon_name_changed(self)

    # when change character level, save all data and re-draw the talent damage
    def character_level_change(self):
        global selected_character
        selected_character = get_character_info(char_name_var.get(), char_level_var.get())

        save_selected_data()
        draw_talent()

    character_label = tk.Label(all_stats_display_app)
    character_label.place(x=10, y=row(0), height=24)
    character_label.configure(text='Character')
    set_color(character_label)

    char_name_choices = sorted(character_name)
    char_name_var = tk.StringVar(all_stats_display_app)
    if 'selected_character' in save_data:
        char_name_var.set(save_data['selected_character'])
    else:
        char_name_var.set(char_name_choices[0])
    char_name_combobox = ttk.Combobox(all_stats_display_app, textvariable=char_name_var, values=char_name_choices)
    char_name_combobox.bind('<<ComboboxSelected>>', character_change)
    char_name_combobox.place(x=70, y=row(0), width=185, height=24)

    char_level_choices = char_level_offset
    char_level_var = tk.StringVar(all_stats_display_app)
    if 'selected_character' in save_data:
        char_level_var.set(save_data['characters'][char_name_var.get()]['level'])
    else:
        char_level_var.set(char_level_offset[len(char_level_offset) - 1])
    char_level_combobox = ttk.Combobox(all_stats_display_app, textvariable=char_level_var, values=char_level_choices)
    char_level_combobox.bind('<<ComboboxSelected>>', character_level_change)
    char_level_combobox.place(x=260, y=row(0), width=78, height=24)

    # change weapon_level ComboBox to match with weapon
    # load weapon_level
    # re-draw talent damage
    # save all selected data
    def weapon_name_changed(self):
        rarity = [weapons_data[i][2] for i, _ in enumerate(weapons_data) if weapons_data[i][0] == weapon_name_var.get()]
        if len(rarity) > 0 and (rarity[0] == 1 or rarity[0] == 2):
            weapons_level = weapons_level_offset[0:19]
        else:
            weapons_level = weapons_level_offset

        if char_name_var.get() in save_data['characters']:
            weapon_level_var.set(save_data['characters'][char_name_var.get()]['weapon_level'])
        elif weapon_level_var.get() not in weapons_level:
            weapon_level_var.set(weapons_level[len(weapons_level) - 1])

        weapon_level_combobox.config(value=weapons_level)

        global selected_weapon
        selected_weapon = get_weapon_info(weapon_name_var.get(), weapon_level_var.get())

        draw_talent()
        save_selected_data()

    def weapon_level_changed(self):
        global selected_weapon
        selected_weapon = get_weapon_info(weapon_name_var.get(), weapon_level_var.get())

        draw_talent()
        save_selected_data()

    weapon_label = tk.Label(all_stats_display_app)
    weapon_label.place(x=10, y=row(1), height=24)
    weapon_label.configure(text='Weapon')
    set_color(weapon_label)

    weapons_name = [weapons_data[i][0] for i, _ in enumerate(weapons_data)]
    weapon_name_choices = sorted(weapons_name)
    weapon_name_var = tk.StringVar(all_stats_display_app)
    if char_name_var.get() in save_data['characters']:
        weapon_name_var.set(save_data['characters'][char_name_var.get()]['weapon'])
    else:
        weapon_name_var.set(weapon_name_choices[0])
    weapon_name_combobox = ttk.Combobox(all_stats_display_app, textvariable=weapon_name_var, values=weapon_name_choices)
    weapon_name_combobox.bind('<<ComboboxSelected>>', weapon_name_changed)
    weapon_name_combobox.place(x=70, y=row(1), width=185, height=24)

    weapon_level_choices = weapons_level_offset
    weapon_level_var = tk.StringVar(all_stats_display_app)
    if 'selected_weapon' in save_data:
        weapon_level_var.set(save_data['characters'][char_name_var.get()]['weapon_level'])
    else:
        weapon_level_var.set(weapons_level_offset[len(weapons_level_offset) - 1])
    weapon_level_combobox = ttk.Combobox(all_stats_display_app, textvariable=weapon_level_var, values=weapon_level_choices)
    weapon_level_combobox.bind('<<ComboboxSelected>>', weapon_level_changed)
    weapon_level_combobox.place(x=260, y=row(1), width=78, height=24)

    def display_artifact(i):
        stats_confirm.artifact_confirm(artifacts[i], alpha, True)

    artifact_label = tk.Label(all_stats_display_app)
    artifact_label.place(x=10, y=row(2), height=24)
    artifact_label.configure(text='Artifact')
    set_color(artifact_label)

    global atf_btn
    artifact_name = ['Flower', 'Plume', 'Sands', 'Goblet', 'Circlet']
    for i in range(5):
        atf_btn[i] = tk.Button(all_stats_display_app)
        atf_btn[i].place(x=70 + (i*55), y=row(2), width=50, height=24)
        atf_btn[i].configure(text=artifact_name[i], state='disabled')
        atf_btn[i].configure(command=lambda atf_i=i: display_artifact(atf_i))
        set_color(atf_btn[i])

    def monster_res_change():
        def set_monster_res():
            global mon_res
            try:
                mon_res = int(monster_res_text.get(1.0, tk.END))
                save_data['mon_res'] = mon_res
                print(f'mon_res= {mon_res}')
            except:
                pass
            monster_res_text.destroy()
            monster_res_confirm_btn.destroy()

            nonlocal monster_res_btn
            monster_res_btn = tk.Button(all_stats_display_app)
            monster_res_btn.place(x=90, y=row(3), width=70, height=24)
            monster_res_btn.configure(text=int(mon_res), command=monster_res_change)
            set_color(monster_res_btn)
            write_save(save_data)
            draw_talent()

        monster_res_btn.destroy()

        monster_res_text = tk.Text(all_stats_display_app)
        monster_res_text.place(x=90, y=row(3), width=35, height=24)
        monster_res_text.insert(1.0, int(mon_res))
        monster_res_text.configure(pady=5)
        set_color(monster_res_text)

        monster_res_confirm_btn = tk.Button(all_stats_display_app)
        monster_res_confirm_btn.place(x=130, y=row(3), width=30, height=24)
        monster_res_confirm_btn.configure(text='Set', command=set_monster_res)
        set_color(monster_res_confirm_btn)

    def monster_lv_change():
        def set_monster_lv():
            global mon_lv
            try:
                mon_lv = int(monster_lv_text.get(1.0, tk.END))
                save_data['mon_lv'] = mon_lv
                print(f'mon_lv= {mon_lv}')
            except:
                pass
            monster_lv_text.destroy()
            monster_lv_confirm_btn.destroy()

            nonlocal monster_lv_btn
            monster_lv_btn = tk.Button(all_stats_display_app)
            monster_lv_btn.place(x=268, y=row(3), width=70, height=24)
            monster_lv_btn.configure(text=int(mon_lv), command=monster_lv_change)
            set_color(monster_lv_btn)
            write_save(save_data)
            draw_talent()

        monster_lv_btn.destroy()

        monster_lv_text = tk.Text(all_stats_display_app)
        monster_lv_text.place(x=268, y=row(3), width=35, height=24)
        monster_lv_text.insert(1.0, int(mon_lv))
        monster_lv_text.configure(pady=5)
        set_color(monster_lv_text)

        monster_lv_confirm_btn = tk.Button(all_stats_display_app)
        monster_lv_confirm_btn.place(x=303, y=row(3), width=30, height=24)
        monster_lv_confirm_btn.configure(text='Set', command=set_monster_lv)
        set_color(monster_lv_confirm_btn)

    global mon_res, mon_lv
    if 'mon_res' in save_data:
        mon_res = save_data['mon_res']
        mon_lv = save_data['mon_lv']

    monster_res_label = tk.Label(all_stats_display_app)
    monster_res_label.place(x=10, y=row(3), height=24)
    monster_res_label.configure(text='Monster RES')
    set_color(monster_res_label)

    monster_res_btn = tk.Button(all_stats_display_app)
    monster_res_btn.place(x=90, y=row(3), width=70, height=24)
    monster_res_btn.configure(text=int(mon_res), command=monster_res_change)
    set_color(monster_res_btn)

    monster_lv_label = tk.Label(all_stats_display_app)
    monster_lv_label.place(x=180, y=row(3), height=24)
    monster_lv_label.configure(text='Monster Level')
    set_color(monster_lv_label)

    monster_lv_btn = tk.Button(all_stats_display_app)
    monster_lv_btn.place(x=268, y=row(3), width=70, height=24)
    monster_lv_btn.configure(text=int(mon_lv), command=monster_lv_change)
    set_color(monster_lv_btn)

    all_stats_display_app.geometry(f'350x200+140+10')

    # refresh weapon name and talent
    character_change(None)

    talent_label = tk.Label(all_stats_display_app)
    talent_label.place(x=10, y=row(4), height=24)
    talent_label.configure(text='Talent Damage', font=('TkDefaultFont', 12))
    set_color(talent_label)

    all_stats_display_app.attributes('-alpha', 0.95)


def main():
    global weapons_data, save_data
    weapons_data = load_weapons_data()
    save_data = read_save()
    load_all_atf()
    draw_window()
    return
