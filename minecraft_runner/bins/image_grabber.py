from PIL import Image, ImageGrab
import pytesseract
import time

psm =''' pagesegmode values are:
  0 = Orientation and script detection (OSD) only.
  1 = Automatic page segmentation with OSD.
  2 = Automatic page segmentation, but no OSD, or OCR
  3 = Fully automatic page segmentation, but no OSD. (Default)
  4 = Assume a single column of text of variable sizes.
  5 = Assume a single uniform block of vertically aligned text.
  6 = Assume a single uniform block of text.
  7 = Treat the image as a single text line.
  8 = Treat the image as a single word.
  9 = Treat the image as a single word in a circle.
  10 = Treat the image as a single character.'''

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
custom_oem_psm_config = r'--oem 3 --psm 7'

# print(pytesseract.image_to_string(Image.open('test.png')))


def screen_shot(coords: tuple):
    whole_screen = ImageGrab.grab()
    whole_screen.save('../.pics/screen.jpg')
    int_part = whole_screen.crop(coords) #left top right bottom
    int_part.save('../.pics/output.jpg')

    result = pytesseract.image_to_string(int_part, config=custom_oem_psm_config)

    return(result, int_part)

def whole_screen_shot():
    whole_screen = ImageGrab.grab()
    whole_screen.save('../.pics/screen.jpg')

    return whole_screen