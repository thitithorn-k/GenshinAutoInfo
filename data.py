import cv2
import numpy as np


# class Data:
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
#     sub_stats_name = [
#         'star', 'hp', 'cri_dmg', 'attack', 'defend', 'cri_rate', 'element', 'energy'
#     ]


load_img = cv2.imread('./data/stats_bw')
load_img_gray = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)

load_data = np.load('./data/data.v4.npy', allow_pickle=True)


def get_data(set):
    dataset = load_data.item().get(set)
    return dataset
