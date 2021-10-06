import cv2
import numpy as np
import re

def run():
    # save_numpy()
    load_numpy()
    pass


def pic(img):
    cv2.imshow('test', img)
    cv2.waitKey()


# for run in Python console Only
def load_numpy():
    load_data = np.load('./data/sub_stat.npy', allow_pickle=True)
    sub = load_data.item().get('sub_stat')
    for i, d in enumerate(sub):
        cv2.imshow(f'{i}', d)


def load_dict(target='./data/data.npy'):
    load = np.load(target, allow_pickle=True)

    dict = {}
    dict['sub_stat_img_set'] = load.item().get('sub_stat_img_set')
    dict['sub_stat_name'] = load.item().get('sub_stat_name')
    dict['number'] = load.item().get('number')
    dict['star'] = load.item().get('star')
    dict['plus'] = load.item().get('plus')
    dict['main_stat_img_set'] = load.item().get('main_stat_img_set')
    dict['main_stat_name'] = load.item().get('main_stat_name')
    dict['artifact_set_img_set'] = load.item().get('artifact_set_img_set')
    dict['artifact_set_name'] = load.item().get('artifact_set_name')
    dict['part_img_set'] = load.item().get('part_img_set')
    dict['part_name'] = load.item().get('part_name')
    return dict


def a():
    b = open('./data/import.txt').read()
    b = b.split('\n')
    for each in b:
        stat = each.split(',')
        char_stat = '{ "atk": ' + stat[4] + '}'
        res = f'\t"level": "{stat[0]}",\n' \
              f'\t"base_hp": {stat[1]},\n' \
              f'\t"base_atk": {stat[2]},\n' \
              f'\t"base_def": {stat[3]},\n' \
              f'\t"char_stat": {char_stat},\n' \
              f'\t"cri_rate": {stat[5]},\n' \
              f'\t"cri_dmg": {stat[6]}\n'
        print('{\n' + res + '},')


def read_talent():
    b = open('./data/import.txt').read()
    b = b.split('\n')
    name = b[0]
    b.remove(b[0])
    res = ''
    res += '{\n' + f'\t"name": "{name}",\n' + '\t"level": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\n'
    res += '\t"detail":[\n'
    for i, each in enumerate(b):
        c = each.split('\t')
        res += '\t\t{\n'
        res += f'\t\t\t"name": "{c[0]}",\n\t\t\t"damage": ['
        del c[0]
        for each_c in c:
            res += f'{each_c}'
            if each_c != c[len(c)-1]:
                res += ', '
        res += ']\n\t\t}'
        if i < len(b)-1:
            res += ','
        res += '\n'
    res += '\t]'
    print(res)

def read_name():
    b = open('./data/import.txt').read()
    line = b.split('\n')
    res = ''
    res += '{\n' + f'\t"name": "{line[0]}",\n\t"status": ' + '{\n'
    line.remove(line[0])
    stat_name = []
    stat_value = []
    s_name = line[0].split('\t')
    line.remove(line[0])
    for each_stat_n in s_name:
        stat_name.append(str.lower(each_stat_n))
        stat_value.append([])
    for each_l in line:
        each = each_l.split('\t')
        for i, e in enumerate(each):
            stat_value[i].append(e)
    for i, each_stat in enumerate(stat_name):
        if i == 4:
            res += '\t\t"char_stat": { '
        else:
            res += '\t\t'
        res += f'"{each_stat}": ['
        for j, each_sub in enumerate(stat_value[i]):
            if i == 0:
                res += '\'' + each_sub + '\''
            else:
                res += each_sub
            if j < len(stat_value[i])-1:
                res += ', '
        res += ']'
        if i == 4:
            res += '}'
        if i < len(stat_name)-1:
            res += ','
        res += '\n'
    res += '\t},\n}'
    print(res)
    return

def low_high(char):
    text = open('./data/import.txt', 'r').read()
    text = re.sub('\n', '', text)
    each_col = text.split('\t')
    low = []
    high = []
    for each in each_col:
        lh = each.split(char)
        low.append(lh[0])
        high.append(lh[1])
    for i, each in enumerate(low):
        print(each, end='')
        if i < len(low)-1:
            print('\t', end='')
    print('\n', end='')
    for i, each in enumerate(high):
        print(each, end='')
        if i < len(low)-1:
            print('\t', end='')


def sumall(char):
    text = open('./data/import.txt', 'r').read()
    line = text.split('\n')
    a = []
    for i in range(15):
        a.append([])
    for i, each_line in enumerate(line):
        if i % 2 == 0:
            each_t = each_line.split('\t')
            for j, each in enumerate(each_t):
                a[j].append(each)
    for i, each_a in enumerate(a):
        for j, each in enumerate(each_a):
            print(each, end='')
            if j < len(each_a)-1:
                print(char, end='')
        if i < len(a):
            print('\t', end='')


def load_test(c_name):
    return eval(open(f'./data/genshin_data/character/{c_name}.json').read())