import cv2
import numpy as np
import reader


# class Data:
#     sub_stats_name = [
#         'star', 'hp', 'cri_dmg', 'attack', 'defend', 'cri_rate', 'element', 'energy'
#     ]
#
#     main_stats_name = [
#         'hp', 'attack', 'element', 'energy', 'physical', 'anemo', 'geo', 'electro', 'hydro', 'pyro', 'cryo', 'cri_rate',
#         'cri_dmg', 'healing'
#     ]
#     star = (0, 0, 18, 18)
#     plus = (0, 138, 10, 148)
#
#     # hp = (0, 18, 72, 32)
#     # cri_dmg = (0, 32, 95, 45)
#     # attack = (0, 45, 81, 61)
#     # defend = (0, 61, 96, 80)
#     # cri_rate = (0, 80, 62, 94)
#     # element = (0, 94, 135, 114)
#     # energy = (0, 114, 142, 138)
#     # all_sub_stat = (0, 0, 152, 138)
#
#     sub_stats_pos = [
#         (0, 0, 18, 18),
#         (0, 18, 82, 32),
#         (0, 32, 105, 45),
#         (0, 45, 91, 61),
#         (0, 61, 106, 80),
#         (0, 80, 72, 94),
#         (0, 94, 145, 114),
#         (0, 114, 152, 138)
#     ]
#
#     number_pos = [
#         (420, 0, 420+30, 40),
#         (144, 0, 144+16, 40),
#         (165, 0, 165+28, 40),
#         (196, 0, 196+28, 40),
#         (227, 0, 227+33, 40),
#         (263, 0, 263+28, 40),
#         (295, 0, 295+30, 40),
#         (326, 0, 326+29, 40),
#         (355, 0, 355+31, 40),
#         (387, 0, 387+29, 40),
#         (144, 41, 144+41, 41+39)  # percent
#     ]
#


load_data = np.load('./data/data.npy', allow_pickle=True)


def get_data(set):
    dataset = load_data.item().get(set)
    return dataset


def add_img_to_set(image, img_set, list_of_name, name):
    load = reader.load_dict()
    i = load[list_of_name].index(name)
    load[img_set][i].append(image)
    np.save('./data/data.npy', load)

    global load_data
    load_data = np.load('./data/data.npy', allow_pickle=True)


def has_percent(stat_name):
    has_p = [
        'hp',
        'atk',
        'def',
        'physical',
        'anemo',
        'geo',
        'electro',
        'hydro',
        'pyro',
        'cryo',
        'cri_rate',
        'cri_dmg',
        'healing'
    ]
    return stat_name in has_p


class Translate:
    en = {
        'hp': 'HP',
        'atk': 'ATK',
        'def': 'DEF',
        'element': 'Elemental Mastery',
        'energy': 'Energy Recharge',
        'physical': 'Physical DMG Bonus',
        'anemo': 'Anemo DMG Bonus',
        'geo': 'Geo DMG Bonus',
        'electro': 'Electro DMG Bonus',
        'hydro': 'Hydro DMG Bonus',
        'pyro': 'Pyro DMG Bonus',
        'cryo': 'Cryo DMG Bonus',
        'cri_rate': 'Crit Rate',
        'cri_dmg': 'Crit DMG',
        'healing': 'Healing Bonus',
        'scan': 'Scan',
        'scan_sam': 'Scan Sample',
        'about': 'About',
        'close': 'Close',
        'confirm': 'Confirm',
        'return': 'Return',
        'main_stat': 'Main stat',
        'sub_stat': 'Sub stat(s)',
        'star': 'Star(s)',
        'level': 'Level',
        'artifact_set': 'Artifact set',
        'add_confirm_caution': 'Add the following image to the dataset to improve the performance of your program',
        'yes': 'Yes',
        'no': 'No',
        'add_confirm_question_start': 'The text on the image above is ',
        'add_confirm_question_end': 'I can read it clearly and\nit doesn\'t have any \'white dot\' on it '
    }
    th = {
        'hp': 'พลังชีวิค',
        'atk': 'พลังโจมตี',
        'def': 'พลังป้องกัน',
        'element': 'ความชำนาญธาตุ',
        'energy': 'การฟื้นฟูพลังงาน',
        'physical': 'โบนัสความเสียหายกายภาพ',
        'anemo': 'โบนัสความเสียหายลม',
        'geo': 'โบนัสความเสียหายหิน',
        'electro': 'โบนัสความเสียหายไฟฟ้า',
        'hydro': 'โบนัสความเสียหายน้ำ',
        'pyro': 'โบนัสความเสียหายไฟ',
        'cryo': 'โบนัสความเสียหายน้ำแข็ง',
        'cri_rate': 'อัตราคริ',
        'cri_dmg': 'แรงคริ',
        'healing': 'โบนัสการรักษา',
        'scan': 'แสกน',
        'scan_sam': 'แสกนตัวอย่าง',
        'about': 'เกี่ยวกับ',
        'close': 'ปิดโปรแกรม',
        'confirm': 'ยืนยัน',
        'return': 'กลับ',
        'main_stat': 'Main stat',
        'sub_stat': 'Sub stat(s)',
        'star': 'จำนวนดาว',
        'level': 'Level',
        'artifact_set': 'Artifact set',
        'add_confirm_caution': 'เพิ่มรูปภาพต่อไปนี้ลงในฐานข้อมูล\nเพื่อปรับปรุงคุณภาพของโปรแกรมของคุณให้ดียิ่งขึ้น',
        'yes': 'ใช่',
        'no': 'ไม่ใช่',
        'add_confirm_question_start': 'ข้อความในภาพด้านบนคือ ',
        'add_confirm_question_end': 'ฉันสามารถอ่านมันได้อย่างง่ายดาย\nและไม่มีจุดสีขาวปะปนอยู่ในภาพ'
    }


language = 1


def get_text(text):
    if text not in Translate.en:
        return text
    if language == 0:
        return Translate.en[text]
    elif language == 1:
        return Translate.th[text]


def get_keys(text):
    if language == 0:
        return list(Translate.en.keys())[list(Translate.en.values()).index(text)]
    elif language == 1:
        return list(Translate.th.keys())[list(Translate.th.values()).index(text)]
