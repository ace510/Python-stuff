from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import time

from PIL import Image
import pytesseract
import pyautogui
import time
from PIL import ImageGrab


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

# time.sleep(10)
whole_screen = ImageGrab.grab()
whole_screen.save('.pics/screen.jpg')
int_part = whole_screen.crop((1500, 1650, 1750, 1735)) #left top right bottom
int_part.save('.pics/output.jpg')
print('here we go')
result = pytesseract.image_to_string(int_part, config=custom_oem_psm_config)

try:
    int(result)
except ValueError:
    int_part.save(f'.pics/{result}.jpg')


# pyautogui.moveTo(2750, 1650)
# pyautogui.click(x=2750, y= 1650, button='left')
# pyautogui.moveTo(2750, 1613)
# pyautogui.click(x=2750, y= 1613)

# for i in range(50):
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(f'X is {currentMouseX}, Y is {currentMouseY}')
#     time.sleep(5)