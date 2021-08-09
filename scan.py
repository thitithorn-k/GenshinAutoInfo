import numpy as np
import imutils
import random

from data import get_data
from image_helper import *

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
        # img_random = 16
        img_name = f'./testim/test-full{img_random}.png'
        img = cv2.imread(img_name)
        print(f'random={img_random}')
    else:
        screen = get_screen()
        if type(screen) is int:
            return -5
        img = np.array(screen)
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
            # cv2.rectangle(find_star, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
            i += 1
            if first_star_pos is None or pt[0] < first_star_pos[0]:
                first_star_pos = pt
    stars_n = i
    if stars_n < 2 or stars_n > 5:
        print('star(s) not found')
        return -1
    # print('stars = ', stars_n)

    # find lime color in image that refer to the artifact set's name ################################
    green_lower = np.array([0, 210, 0], np.uint8)
    green_upper = np.array([200, 255, 200], np.uint8)
    green_mask = cv2.inRange(long_stats, green_lower, green_upper)
    green_mask = cv2.cvtColor(green_mask, cv2.COLOR_GRAY2BGR) != 0
    artifact_set = long_stats * green_mask
    # cv2.imshow('testing2', artifact_set)

    green_mask_cont, _, _ = find_contours(artifact_set, 0, (15, 2), (0, 255))
    asn_pos = get_pos_from_contours(green_mask_cont)  # artifact set name's position

    # cut needless part from 'long_stats'
    top_asn = len(asn_pos)-1
    if top_asn < 0:  # exit if artifact-set's name is not found
        print('artifact-set\'s name not found')
        return -2
    asn_y = asn_pos[top_asn][1] + asn_pos[top_asn][3]
    status_crop = long_stats[0:asn_y, 0:230]

    all_cnts, status_crop_gray, status_crop_bw = find_contours(status_crop, 0, (15, 2), (190, 255))
    all_stats_pos = get_pos_from_contours(all_cnts)

    # draw rect over contours of each stat
    # status_crop_rect, _ = draw_rect_from_contours(status_crop, all_cnts)
    # cv2.imshow(f'status_crop_rect', status_crop_rect) # Show color+rect

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
        print('Too much sub stats, something went wrong.')
        return -3

    # find level position
    level_pos = (first_star_pos[0]+5, first_star_pos[1]+30, 32, 18)
    level_img = find_star[level_pos[1]:level_pos[1]+level_pos[3], level_pos[0]:level_pos[0]+level_pos[2]]
    # cv2.imshow('level', level_img)
    level = read_level(level_img)

    # split all position of each stats to var
    sub_stat_pos = []
    sub_stat_crop = []
    for i in range(sub_stats_n):
        sub_stat_pos.append(all_stats_pos[i + 1])
        # find_star = draw_rect_from_pos(find_star, sub_stat_pos[i])
        sub_stat_crop.append(long_stats[sub_stat_pos[i][1]:sub_stat_pos[i][1]+sub_stat_pos[i][3], sub_stat_pos[i][0]:sub_stat_pos[i][0]+sub_stat_pos[i][2]])
        # cv2.imshow(f'sub_stat_crop_{i}', sub_stat_crop[i])

    # reverse array to make it top to bottom
    sub_stat_crop = sub_stat_crop[::-1]
    sub_stat_pos = sub_stat_pos[::-1]

    main_stat_pos = (first_star_pos[0], first_star_pos[1] - 39, 220, 30)
    main_stat_crop = long_stats[main_stat_pos[1]:main_stat_pos[1] + main_stat_pos[3], main_stat_pos[0]:main_stat_pos[0] + main_stat_pos[2]]
    # cv2.imshow('main_stat_crop', main_stat_crop)

    artifact_part_pos = (first_star_pos[0], first_star_pos[1] - 64, 160, 22)
    artifact_part_crop = long_stats[artifact_part_pos[1]:artifact_part_pos[1] + artifact_part_pos[3], artifact_part_pos[0]:artifact_part_pos[0] + artifact_part_pos[2]]
    part_name, part_name_img_bw = read_part(artifact_part_crop)

    # find_star = draw_rect_from_pos(find_star, main_stat_pos)
    # cv2.imshow(f'find_star', find_star)

    main_stat_crop_name, main_stat_crop_value = split_main_stat_name_and_value(main_stat_crop)
    if type(main_stat_crop_name) is int and main_stat_crop_value == -1:
        print('Main stat not found')
        return -4
    main_stat_name, main_stat_name_img_bw = match_image_with_set_and_name([main_stat_crop_name], 'main_stat_img_set', 'main_stat_name')
    main_stat_name = main_stat_name[0]
    main_stat_name_img_bw = main_stat_name_img_bw[0]
    main_stat_value = read_value([main_stat_crop_value])

    # split sub_stat_crop to name and value
    sub_stat_crop_name = []
    sub_stat_crop_value = []
    for each_sub_stat_crop in sub_stat_crop:
        name, value = split_sub_stat_name_and_value(each_sub_stat_crop)
        sub_stat_crop_name.append(name)
        sub_stat_crop_value.append(value)

    sub_stat_name, sub_stat_name_img_bw = match_image_with_set_and_name(sub_stat_crop_name, 'sub_stat_img_set', 'sub_stat_name')
    sub_stat_value = read_value(sub_stat_crop_value)

    # add all info to dictionary and return
    res = {}
    res['artifact_status_img'] = status_crop
    res['star'] = stars_n
    res['level'] = level
    res['part_name'] = part_name
    res['part_name_img_bw'] = part_name_img_bw
    res['main_stat_name'] = main_stat_name
    res['main_stat_value'] = main_stat_value[0]
    res['main_stat_name_img_bw'] = main_stat_name_img_bw
    res['sub_stat_name'] = sub_stat_name
    res['sub_stat_value'] = sub_stat_value
    res['sub_stat_name_img_bw'] = sub_stat_name_img_bw

    return res

# read name of part of artifact
# return part name, bw_img of part
def read_part(part_img):
    part_img_cont, _, _ = find_contours(part_img, 0, (10, 8))
    part_img_cut = cut_image_from_contours(part_img, part_img_cont)
    largest = 0
    if len(part_img_cut) > 1:
        for i, each_part_img_cut in part_img_cut:
            if each_part_img_cut.shape[0] > part_img_cut[largest].shape[0]:
                largest = i
    part_img_cut = part_img_cut[largest]
    # cv2.imshow(f'part_cut', part_img_cut)
    part_name, part_img_bw = match_image_with_set_and_name([part_img_cut], 'part_img_set', 'part_name')
    return part_name[0], part_img_bw[0]

# read level of artifact
# return int
def read_level(level_img):
    level = read_value([level_img], True)[0][0]
    if level > 100:
        level %= 100
    else:
        level %= 10
    if level < 0 or level > 20:
        level = 0
    level = int(level)
    return level

# split full main stat crop to its name abd value img
# return main_stat_name_img, main_stat_value_img
def split_main_stat_name_and_value(main_stat_crop_img):
    main_stat_crop_img_cont, _, _ = find_contours(main_stat_crop_img, 0, (10, 30), (200, 255))
    cut_main_stat = cut_image_from_contours(main_stat_crop_img, main_stat_crop_img_cont, True)
    if len(cut_main_stat) != 2:
        return -1, -1
    # for i, each_cut in enumerate(cut_main_stat):
    #     cv2.imshow(f'{i}cut_main', each_cut)
    return cut_main_stat[1], cut_main_stat[0]


# split full sub stat crop to its name and value img
# return [name:Image, value:Image]
def split_sub_stat_name_and_value(sub_stat_crop_img):
    plus_img_gray = get_data('plus')

    sub_stat_crop_img_grey = cv2.cvtColor(sub_stat_crop_img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(sub_stat_crop_img_grey, plus_img_gray, cv2.TM_CCOEFF_NORMED)

    _, _, _, max_match_pos = cv2.minMaxLoc(res)
    h, w, _ = sub_stat_crop_img.shape
    return sub_stat_crop_img[0:h, 0:max_match_pos[0]], sub_stat_crop_img[0:h, max_match_pos[0]+10:w]


# read number of the array of sub_stat_crop_value's image
# return array[value_of_stat:int, is it percent: bool]
def read_value(stat_value, adaptive_color=True):
    if len(stat_value) <= 0:
        return
    result = []
    for a, stat_value_img in enumerate(stat_value):
        # cv2.imshow('sub',stat_value_img)

        stat_value_img = imutils.resize(stat_value_img, height=105)

        # cv2.imshow(f'{a}sub_resize', stat_value_img)
        if adaptive_color:
            mean = cv2.mean(stat_value_img)
            mean = np.mean(mean)
            if mean > 123:
                adaptive = 180
            elif mean > 120:
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
                adaptive = 145
        else:
            adaptive = 230

        stat_value_cont, _, stat_value_img_bw = find_contours(stat_value_img, 0, (1, 60), (adaptive, 255))
        cut_num = cut_image_from_contours(stat_value_img_bw, stat_value_cont, True)

        dataset_num = []
        dataset_number = get_data('number')
        for each_num_img in dataset_number:
            num_img = imutils.resize(each_num_img, height=100)
            dataset_num.append(num_img)

        percent = 0
        value = 0
        decimal = 0
        error = 0
        cut_error = 0

        for i, each_cut_num in enumerate(cut_num):
            each_cut_num_cont = cv2.findContours(each_cut_num, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            each_cut_num_cont = imutils.grab_contours(each_cut_num_cont)
            each_cut_num_no_outer = cut_image_from_contours(each_cut_num, each_cut_num_cont)
            each_cut_num = None
            for each_no_outer in each_cut_num_no_outer:
                if each_cut_num is None or each_cut_num.shape[0] < each_no_outer.shape[0]:
                    each_cut_num = each_no_outer

            if each_cut_num.shape[0] < 45 and each_cut_num.shape[1] < 45:  # if it's 'dot'
                if decimal == 0 and i != 0 and i-percent < 3:
                    value *= 1/(10**(i-percent+cut_error))
                    decimal = i
                else:
                    error += 1
            else:
                each_cut_num = imutils.resize(each_cut_num, height=100)
                if each_cut_num.shape[1] < 45 and each_cut_num.shape[0] > 45:  # if it's 1
                    value += 1*(10**(i-percent-decimal-error+cut_error))
                else:
                    each_cut_num_expand = cv2.copyMakeBorder(each_cut_num, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])

                    most_match = [None, None]
                    most_match_i = [None, None]
                    most_match_loc = [None, None]
                    for j, each_temp_num in enumerate(dataset_num):
                        if j == 1:
                            continue
                        # cv2.imshow(f'{j}eeee', each_temp_num)
                        res = cv2.matchTemplate(each_cut_num_expand, each_temp_num, cv2.TM_CCOEFF_NORMED)
                        threshold = 0.6
                        loc = np.where(res >= threshold)
                        max_res = cv2.minMaxLoc(res)[1]

                        if most_match[0] is None or max_res > most_match[0]:
                            most_match[1] = most_match[0]
                            most_match_i[1] = most_match_i[0]
                            most_match_loc[1] = most_match_loc[0]
                            most_match[0] = max_res
                            most_match_i[0] = j
                            most_match_loc[0] = cv2.minMaxLoc(res)
                    # cv2.imshow(f'num-{i}-{most_match_i}', get_gray_image(Data.number_pos[most_match_i]))

                    # if 2 number is in the same image. this will help to split it and fix the value
                    if each_cut_num.shape[1] > 110:
                        if most_match_loc[0][2][0] < most_match_loc[1][2][0]:
                            most_match_i = most_match_i[::-1]
                            value += most_match_i[1] * (10**(i-percent-decimal-error+cut_error))
                            cut_error += 1

                    if most_match_i[0] == 10:
                        percent = 1
                        value = 0
                    else:
                        value += most_match_i[0] * (10**(i-percent-decimal-error+cut_error))
        # print(value, '%' if percent else '')
        result.append([value, True if percent else False])
    return result




