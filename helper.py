import cv2
from PIL import ImageGrab
import win32gui
import imutils
import data


def draw_rect_from_contours(image, contours, only=-1, smallest_size=(5, 5)):
    new_image = image.copy()
    drawn = 0
    pos = []
    for (i, c) in enumerate(contours):

        (x, y, w, h) = cv2.boundingRect(c)

        if w > smallest_size[0] and h > smallest_size[1]:
            drawn += 1
            if only != -1 and drawn-1 != only:
                continue
            cv2.rectangle(new_image, (x - 2, y - 3), ((x + w + 2), (y + h + 2)), (0, 0, 255), 1)
            pos.append((x, y, w, h))

    return new_image, pos


def draw_rect_from_pos(image, pos):
    new_image = image
    cv2.rectangle(new_image, (pos[0]-1, pos[1]-3),(pos[0] + pos[2] + 2, pos[1] + pos[3] + 2), (0, 0, 255), 1)
    return new_image


def get_pos_from_contours(contours, smallest_size=(5, 5)):
    pos = []
    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        if w > smallest_size[0] and h > smallest_size[1]:
            pos.append((x, y-1 if y-1 >= 0 else 0, w, h))

    return pos


def get_screen():
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    genshin = [(hwnd, title) for hwnd, title in winlist if ('genshin impact' or '原神') in title.lower()]
    if not genshin:
        print('not found genshin\'s window')
        return

    hwnd = genshin[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)

    return img


# mode
# 0 = BGR
# 1 = gray
# 2 = bw
def find_contours(image, mode=0, kernel=(1, 10), thresh=(150, 255)):
    image_gray = image
    image_bw = image
    if mode == 0:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if mode <= 1:
        image_bw = cv2.threshold(image_gray, thresh[0], thresh[1], cv2.THRESH_BINARY)[1]
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel)
    image_morp = cv2.morphologyEx(image_bw, cv2.MORPH_CLOSE, rect_kernel)
    image_cont = cv2.findContours(image_morp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    res_cont = imutils.grab_contours(image_cont)

    return res_cont, image_gray, image_bw


def cut_image_from_contours(image, contours, right_to_left=False):
    pos = get_pos_from_contours(contours)

    if right_to_left:
        pos_temp = []
        pos_len = len(pos)
        for i in range(pos_len):
            rightest = pos[0]
            for j, each_pos in enumerate(pos):
                if each_pos[0] > rightest[0]:
                    rightest = each_pos
            pos_temp.append(rightest)
            pos.remove(rightest)
        pos = pos_temp
        # print(pos)

    result = []
    for each_pos in pos:
        # print(each_pos)
        result.append(image[each_pos[1]:each_pos[1]+each_pos[3], each_pos[0]:each_pos[0]+each_pos[2]])
    return result


def match_image_with_set_and_name(image_array, set_img, set_name):
    result = []
    match_i = []
    if len(image_array) > 0:
        for each_image in image_array:
            each_image_gray = cv2.cvtColor(each_image, cv2.COLOR_BGR2GRAY)
            each_image_bw = cv2.threshold(each_image_gray, 180, 255, cv2.THRESH_BINARY)[1]
            each_image_border = cv2.copyMakeBorder(each_image_bw, 10, 10, 50, 50, cv2.BORDER_CONSTANT,
                                                   value=[0, 0, 0])
            most_match = None
            most_match_i = None
            compare_img_set = data.get_data(set_img)
            for o, each_compare_img_set in enumerate(compare_img_set):
                for each_compare_img in each_compare_img_set:

                    res = cv2.matchTemplate(each_image_border, each_compare_img, cv2.TM_CCOEFF_NORMED)
                    max_res = cv2.minMaxLoc(res)[1]
                    if most_match is None or max_res > most_match:
                        most_match = max_res
                        most_match_i = o

            match_i.append(most_match_i)

        # print each sub stat text
        for each_i in match_i:
            result.append(data.get_data(set_name)[each_i])

    return result
