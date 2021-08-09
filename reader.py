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

