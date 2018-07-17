import sys
from pytesseract import image_to_string
from PIL import Image
import cv2 as cv



def get_image(filename):
    return Image.open(filename)
    #return cv.imread(filename)

if __name__ == '__main__' :
    img = get_image('textimg.jpg')
    sys.stdout.write('=== TEXT FROM IMAGE ==='+'\n')

    sys.stdout.write(image_to_string(img, lang = "kor"))