import numpy as np
import imutils
import random

from data import get_data
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

test_image2 = (
    './testim/test4.png',
    './testim/test-full2.png',
    './testim/test-full3.png',

    './testim/test-full5.png',

    './testim/test-full7.png',

    './testim/test-full9.png',

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

# stars_n = number of artifact's stars
# sub_stats_n = number of artifact's sub stats
####################################################################


def run(test=False):
    cv2.destroyAllWindows()

    img = None
    if test:
        img_random = random.randint(1, 19)
        img_name = f'./testim/test-full{img_random}.png'
        img = cv2.imread(img_name)
        print(f'random={img_random}')
    else:
        img = np.array(get_screen())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize and cut the image long enough to see all stats
    img720 = imutils.resize(img, width=1280)
    long_stats = img720[82:82 + 370, 976:976 + 230]
    # cv2.imshow('long_stats', long_stats)

    # use gray image to find the star_img_gray ######################################################
    long_stats_gray = cv2.cvtColor(long_stats, cv2.COLOR_BGR2GRAY)
    find_star = long_stats_gray

    # load star_img_gray image from data.py, change it to gray scale
    # and put size of it to var
    star_img_gray = get_data('star')
    w, h = star_img_gray.shape[::-1]

    # each_sub_stat_crop_gray any star_img_gray and draw rect over it
    # save the first_star_pos star_img_gray (most left star_img_gray) position to 'first_star_pos'
    # print number of star_img_gray
    res = cv2.matchTemplate(find_star, star_img_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    i = 0
    mask = np.zeros(find_star.shape[:2], np.uint8)
    first_star_pos = None
    find_star = long_stats
    for pt in zip(*loc[::-1]):
        if mask[pt[1] + int(round(h / 2)), pt[0] + int(round(w / 2))] != 255:
            mask[pt[1]:pt[1] + h, pt[0]:pt[0] + w] = 255
            cv2.rectangle(find_star, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
            i += 1
            if first_star_pos is None or pt[0] < first_star_pos[0]:
                first_star_pos = pt
    stars_n = i
    print('stars = ', stars_n)

    # find lime color in image that refer to the artifact set's name ################################
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
    top_asn = len(asn_pos)-1
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
    status_crop_rect, _ = draw_rect_from_contours(status_crop, all_cnts)
    cv2.imshow(f'status_crop_rect', status_crop_rect) # Show color+rect

    # count sub stats by high from star_img_gray to the end of picture
    star_to_end = asn_y - first_star_pos[1]
    sub_stats_n = 0
    if star_to_end < 90:
        pass
    elif star_to_end < 116:
        sub_stats_n = 1
    elif star_to_end < 136:
        sub_stats_n = 2
    elif star_to_end < 160:
        sub_stats_n = 3
    elif star_to_end < 180:
        sub_stats_n = 4
    else:
        print('too long sub stats, something went wrong.')
        return

    # find level position
    level_pos = (first_star_pos[0]+5, first_star_pos[1]+30, 32, 18)
    level_img = find_star[level_pos[1]:level_pos[1]+level_pos[3], level_pos[0]:level_pos[0]+level_pos[2]]
    # cv2.imshow('level', level_img)

    # split all position of each stats to var
    sub_stat_pos = []
    sub_stat_crop = []
    for i in range(sub_stats_n):
        sub_stat_pos.append(all_stats_pos[i + 1])
        find_star = draw_rect_from_pos(find_star, sub_stat_pos[i])
        sub_stat_crop.append(long_stats[sub_stat_pos[i][1]:sub_stat_pos[i][1]+sub_stat_pos[i][3], sub_stat_pos[i][0]:sub_stat_pos[i][0]+sub_stat_pos[i][2]])
        # cv2.imshow(f'sub_stat_crop_{i}', sub_stat_crop[i])

    # reverse array to make it top to bottom
    sub_stat_crop = sub_stat_crop[::-1]
    sub_stat_pos = sub_stat_pos[::-1]

    main_stat_pos = (first_star_pos[0], first_star_pos[1] - 39, 220, 30)
    main_stat_crop = long_stats[main_stat_pos[1]:main_stat_pos[1] + main_stat_pos[3], main_stat_pos[0]:main_stat_pos[0] + main_stat_pos[2]]
    cv2.imshow('main_stat_crop', main_stat_crop)

    find_star = draw_rect_from_pos(find_star, main_stat_pos)

    cv2.imshow(f'find_star', find_star)
    # return main_stat_crop

    # np.save('data1.npy', sub_stat_crop)

    # ==========================================================================

    # split sub_stat_crop to name and value
    sub_stat_crop_name = []
    sub_stat_crop_value = []
    for each_sub_stat_crop in sub_stat_crop:
        name, value = split_sub_stat_name_and_value(each_sub_stat_crop)
        sub_stat_crop_name.append(name)
        sub_stat_crop_value.append(value)

    sub_stat_name = read_sub_stat_name(sub_stat_crop_name)
    sub_stat_value = read_sub_stat_value(sub_stat_crop_value)

    if sub_stat_name:
        print('sub stat ==================================')
        for i, each_sub in enumerate(sub_stat_name):
            print(each_sub, '+', sub_stat_value[i][0], '%' if sub_stat_value[i][1] else '')
    else:
        print('This artifact doesn\'t have sub stats')

    print('===========================================')

    split_main_stat_name_and_value(main_stat_crop)


def split_main_stat_name_and_value(main_stat_crop_img):
    main_stat_crop_img_gray = cv2.cvtColor(main_stat_crop_img, cv2.COLOR_BGR2GRAY)
    main_stat_crop_img_bw = cv2.threshold(main_stat_crop_img_gray, 200, 255, cv2.THRESH_BINARY)[1]

    main_stat_rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 30))
    main_stat_crop_img_morp = cv2.morphologyEx(main_stat_crop_img_bw, cv2.MORPH_CLOSE, main_stat_rect_kernel)
    main_stat_crop_img_cont = cv2.findContours(main_stat_crop_img_morp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    main_stat_crop_img_cont = imutils.grab_contours(main_stat_crop_img_cont)

    cut_main_stat = cut_image_from_contours(main_stat_crop_img_bw, main_stat_crop_img_cont, True)
    for i, each_cut in enumerate(cut_main_stat):
        cv2.imshow(f'{i}cut_main', each_cut)


# split full sub stat crop to it's name and value
# return [name:Image, value:Image]
def split_sub_stat_name_and_value(sub_stat_crop_img):
    plus_img_gray = get_data('plus')

    sub_stat_crop_img_grey = cv2.cvtColor(sub_stat_crop_img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(sub_stat_crop_img_grey, plus_img_gray, cv2.TM_CCOEFF_NORMED)

    _, _, _, max_match_pos = cv2.minMaxLoc(res)
    h, w, _ = sub_stat_crop_img.shape
    return sub_stat_crop_img[0:h, 0:max_match_pos[0]], sub_stat_crop_img[0:h, max_match_pos[0]+10:w]


# read text of the array of sub stat_crop_name's image
# return array[name_of_stat:String]
def read_sub_stat_name(sub_stat_name_img):
    result = []
    sub_stat_i = []
    if len(sub_stat_name_img) > 0:
        for each_sub_stat_name in sub_stat_name_img:
            each_sub_stat_name_gray = cv2.cvtColor(each_sub_stat_name, cv2.COLOR_BGR2GRAY)

            o = 0
            most_match = None
            most_match_i = None
            sub_stat_img = get_data('sub_stat_img')
            for o, each_stat_img in enumerate(sub_stat_img):
                compare_stat_gray = each_stat_img
                each_sub_stat_name_bw = cv2.threshold(each_sub_stat_name_gray, 180, 255, cv2.THRESH_BINARY)[1]
                each_sub_stat_name_bw = cv2.copyMakeBorder(each_sub_stat_name_bw, 10, 10, 50, 50, cv2.BORDER_CONSTANT,
                                                           value=[0, 0, 0])
                res = cv2.matchTemplate(each_sub_stat_name_bw, compare_stat_gray, cv2.TM_CCOEFF_NORMED)
                max_res = cv2.minMaxLoc(res)[1]
                if most_match is None or max_res > most_match:
                    most_match = max_res
                    most_match_i = o

            sub_stat_i.append(most_match_i)

        # print each sub stat text
        for each in sub_stat_i:
            result.append(get_data('sub_stat_name')[each])
    else:
        print('This artifact don\'t have sub stats.')

    return result


# read number of the array of sub_stat_crop_value's image
# return array[value_of_stat:int, is it percent: bool]
def read_sub_stat_value(sub_stat_value):
    if len(sub_stat_value) <= 0:
        return
    result = []
    for a, sub_stat_value_img in enumerate(sub_stat_value):
        # cv2.imshow('sub',sub_stat_value_img)

        sub_stat_value_img = imutils.resize(sub_stat_value_img, height=105)

        # cv2.imshow(f'{a}sub_resize', sub_stat_value_img)
        mean = cv2.mean(sub_stat_value_img)
        mean = np.mean(mean)
        if mean > 120:
            adaptive = 170
        elif mean > 110:
            adaptive = 165
        elif mean > 107:
            adaptive = 160
        elif mean > 102:
            adaptive = 150
        elif mean > 97:
            adaptive = 145
        else:
            adaptive = 140

        sub_stat_value_img_gray = cv2.cvtColor(sub_stat_value_img, cv2.COLOR_BGR2GRAY)
        sub_stat_value_img_bw = cv2.threshold(sub_stat_value_img_gray, adaptive, 255, cv2.THRESH_TOZERO)[1]
        cv2.imshow(f'{a}testaaa', sub_stat_value_img_bw)
        sub_stat_value_img_bw_for_match = cv2.threshold(sub_stat_value_img_gray, adaptive, 255, cv2.THRESH_BINARY)[1]

        rect_num_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 100))
        sub_stat_value_img_morp = cv2.morphologyEx(sub_stat_value_img_bw, cv2.MORPH_CLOSE, rect_num_kernel)
        cv2.imshow(f'{a}testabbbaa', sub_stat_value_img_morp)

        sub_stat_value_cont = cv2.findContours(sub_stat_value_img_morp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        sub_stat_value_cont = imutils.grab_contours(sub_stat_value_cont)

        cut_num = cut_image_from_contours(sub_stat_value_img_bw_for_match, sub_stat_value_cont, True)

        temp_num = []
        number = get_data('number')
        for each_num_img in number:
            num_img = imutils.resize(each_num_img, height=100)
            temp_num.append(num_img)

        percent = 0
        value = 0
        decimal = 0

        for i, each_cut_num in enumerate(cut_num):
            # cv2.imshow(f'{a}cut{i}', each_cut_num)
            if each_cut_num.shape[0] < 45 and each_cut_num.shape[1] < 45:  # if it's 'dot'
                if decimal == 0 and i != 0:
                    value *= 1/(10**(i-percent))
                    decimal = i
            elif each_cut_num.shape[1] < 45 and each_cut_num.shape[0] > 45:  # if it's 1
                value += 1*(10**(i-percent-decimal))
            else:
                pass
                each_cut_num_expand = cv2.copyMakeBorder(each_cut_num, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])

                most_match = None
                most_match_i = None
                for j, each_temp_num in enumerate(temp_num):
                    if j == 1:
                        continue
                    # cv2.imshow(f'{j}eeee', each_temp_num)
                    res = cv2.matchTemplate(each_cut_num_expand, each_temp_num, cv2.TM_CCOEFF_NORMED)
                    threshold = 0.6
                    loc = np.where(res >= threshold)
                    max_res = cv2.minMaxLoc(res)[1]
                    if most_match is None or max_res > most_match:
                        most_match = max_res
                        most_match_i = j
                # cv2.imshow(f'num-{i}-{most_match_i}', get_gray_image(Data.number_pos[most_match_i]))

                if most_match_i == 10:
                    percent = 1
                    value = 0
                else:
                    value += most_match_i * (10**(i-percent-decimal))
        # print(value, '%' if percent else '')
        result.append([value, True if percent else False])
    return result




