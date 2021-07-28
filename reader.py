import cv2
import numpy as np

def run():
    # save_numpy()
    load_numpy()
    pass

# for run in Python console Only
def load_numpy():
    load_data = np.load('./data/sub_stat.npy', allow_pickle=True)
    sub = load_data.item().get('sub_stat')
    for i, d in enumerate(sub):
        cv2.imshow(f'{i}', d)


def load_dict():
    load = np.load('./data/data.v2.npy', allow_pickle=True)

    dict = {}
    dict['sub_stat_img'] = load.item().get('sub_stat_img')
    dict['sub_stat_name'] = load.item().get('sub_stat_name')
    dict['number'] = load.item().get('number')
    dict['star'] = load.item().get('star')
    dict['plus'] = load.item().get('plus')

    return dict

