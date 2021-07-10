from imutils import contours
import numpy
import argparse
import imutils
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


def read():
    print('read')

    # text = pytesseract.image_to_string(img)
    # print(text)


def read_img(img):
    text = pytesseract.image_to_string(img, lang="tha+eng", timeout=2)
    print(text)
