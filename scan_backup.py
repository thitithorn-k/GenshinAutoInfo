import numpy as np
import imutils
import random

import data
from helper import *

from data import *

test_image = (
    './testim/test4.png',
    './testim/test-full2.png',
    './testim/test-full3.png',
    './testim/test-full4.png',
    './testim/test-full5.png',
    './testim/test-full6.png',
    './testim/test-full7.png',
    './testim/test-full8.png',
    './testim/test-full9.png',
    './testim/test-full10.png',
    './testim/test-full11.png'
)


####################################################################
# stats-position variable description
####################################################################
# all_stats_pos = all of stats position (x, y, w, h)
# asn_pos[top_asn] = artifact-set's name position (x, y, w, h)
# first_star_pos = artifact star position (x, y)
# level_pos = artifact level position (x, y, w, h)
# sub_stat_pos = array of sub stat position [(x, y, w, h)]
####################################################################


def run(test=False):
    img = None
    if test:
        img = cv2.imread(test_image[random.randint(0, len(test_image) - 1)])
    else:
        img = np.array(get_screen())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize and cut the image long enough to see all stats
    img720 = imutils.resize(img, width=1280)
    long_stats = img720[82:82 + 370, 976:976 + 230]
    cv2.imshow('long_stats', long_stats)

    # find lime color in image that refer to the artifact set's name
    green_lower = np.array([0, 210, 0], np.uint8)
    green_upper = np.array([200, 255, 200], np.uint8)
    green_mask = cv2.inRange(long_stats, green_lower, green_upper)
    green_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR) != 0
    artifact_set = long_stats * green_mask
    # cv2.imshow('testing2', artifact_set)

    # setup rect-angel kernel
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 2))

    # change artifact-set's name to black n white rectangle
    green_mask_gray = cv2.cvtColor(artifact_set, cv2.COLOR_BGR2GRAY)
    green_mask_bw = cv2.threshold(green_mask_gray, 0, 255, cv2.THRESH_BINARY)[1]
    green_mask_bw_morph = cv2.morphologyEx(green_mask_bw, cv2.MORPH_CLOSE, rect_kernel)
    green_mask_bw_thres = cv2.threshold(green_mask_bw_morph, 0, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('green_mask_bw_thres', green_mask_bw_thres)

    # find location of artifact-set's name
    green_mask_bw_thres_cnts = cv2.findContours(green_mask_bw_thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    green_mask_bw_thres_cnts = imutils.grab_contours(green_mask_bw_thres_cnts)
    asn_pos = get_pos_from_contours(green_mask_bw_thres_cnts)  # artifact set name's position

    # cut needless part from 'long_stats'
    top_asn = len(asn_pos) - 1
    if top_asn < 0:  # exit if artifact-set's name is not found
        print('artifact-set\'s name not found')
        return
    asn_y = asn_pos[top_asn][1] + asn_pos[top_asn][3]
    status_crop = long_stats[0:asn_y, 0:230]

    # change status_crop to black and white color
    status_crop_gray = cv2.cvtColor(status_crop, cv2.COLOR_BGR2GRAY)
    status_crop_bw = cv2.threshold(status_crop_gray, 190, 240, cv2.THRESH_BINARY)[1]
    status_crop_morph = cv2.morphologyEx(status_crop_bw, cv2.MORPH_CLOSE, rect_kernel)
    status_crop_thres = cv2.threshold(status_crop_morph, 0, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('status_crop_thres', status_crop_thres)

    # find contours of status_crop_thres
    all_cnts = cv2.findContours(status_crop_thres.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    all_cnts = imutils.grab_contours(all_cnts)
    all_stats_pos = get_pos_from_contours(all_cnts)

    # draw rect over contours of each stat
    status_crop_rect, pos = draw_rect_from_contours(status_crop, all_cnts)
    cv2.imshow(f'status_crop_rect', status_crop_rect)  # Show color+rect

    # use gray image to find the star_img ######################################################
    find_star = status_crop_gray

    # load star_img image from data.py, change it to gray scale
    # and put size of it to var
    star_img = get_gray_image(data.star)
    star_img = cv2.cvtColor(star_img, cv2.COLOR_BGR2GRAY)
    w, h = star_img.shape[::-1]

    # match any star_img and draw rect over it
    # save the first_star_pos star_img (most left star_img) position to 'first_star_pos'
    # print number of star_img
    res = cv2.matchTemplate(find_star, star_img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    i = 0
    mask = np.zeros(find_star.shape[:2], np.uint8)
    first_star_pos = None
    find_star = status_crop
    for pt in zip(*loc[::-1]):
        if mask[pt[1] + int(round(h / 2)), pt[0] + int(round(w / 2))] != 255:
            mask[pt[1]:pt[1] + h, pt[0]:pt[0] + w] = 255
            cv2.rectangle(find_star, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
            i += 1
            if first_star_pos is None or pt[0] < first_star_pos[0]:
                first_star_pos = pt
    print('star_img=', i)

    # count sub stats by high from star_img to the end of picture
    star_to_end = asn_y - first_star_pos[1]
    sub_stats_n = 0
    if star_to_end < 90:
        sub_stats_n = 0
    elif star_to_end < 116:
        sub_stats_n = 1
    elif star_to_end < 136:
        sub_stats_n = 2
    elif star_to_end < 160:
        sub_stats_n = 3
    elif star_to_end < 180:
        sub_stats_n = 4
    else:
        print('too long sub stats, something wrong')

    # draw rect over level of artifact by plus offset from first star_img
    level_pos = (first_star_pos[0], first_star_pos[1] + 28, 38, 20)
    cv2.rectangle(find_star, (level_pos[0], level_pos[1]), (level_pos[0] + level_pos[2], level_pos[1] + level_pos[3]),
                  (0, 0, 255), 1)
    # find_star = cv2.cvtColor(find_star, cv2.COLOR_GRAY2RGB)
    # cv2.imshow(f'find_star', find_star)  # use 'do' to define each window

    # split all position of each stats to var
    sub_stat_pos = []
    for i in range(sub_stats_n):
        sub_stat_pos.append(all_stats_pos[i + 1])
        find_star = draw_rect_from_pos(find_star, sub_stat_pos[i])

    main_stat = (first_star_pos[0], first_star_pos[1] - 39, 220, 30)
    find_star = draw_rect_from_pos(find_star, main_stat)

    cv2.imshow(f'find_star', find_star)




