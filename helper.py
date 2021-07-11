import cv2
from PIL import ImageGrab
import win32gui


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

    genshin = genshin[0]
    hwnd = genshin[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)

    return img


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