try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
reroll_button = (1843, 1323)
stat_range = set()

# pyautogui.moveRel(None, 10)
# pytesseract.image_to_string(Image.open('image.name'))
keepgoing = True

while keepgoing:
    imgString = ""
    pyautogui.moveTo(1843, 1360)
    pyautogui.click(x=1843, y=1360, button="left")
    pyautogui.moveTo(1843, 1323)
    pyautogui.click(x=1843, y=1323)

    gameScreenshot = pyautogui.screenshot()
    shotCrop = gameScreenshot.crop((1772, 1265, 1808, 1292))
    # shotCrop.save(r'.\screenshot.png')

    # img = Image.open(r'.\screenshot.png')
    imgString = pytesseract.image_to_string(shotCrop, config="--psm 8")
    print(imgString)
    try:
        imgInt = int(imgString)
    except ValueError:
        if imgString in ("\\ a", "IAT,"):
            imgInt = 77
        elif imgString in ("si"):
            imgInt = 81
        elif imgString in ("sw"):
            imgInt = 87
        elif imgString in ("see"):
            imgInt = 82
        elif imgString in ("el"):
            imgInt = 83
        elif imgString in ("et"):
            imgInt = 84
        elif imgString in ("oli"):
            imgInt = 91
        else:
            break

    print(imgInt)
    stat_range.add(imgInt)

    if imgInt > 90 or imgInt < 20:
        keepgoing = False


"""
for i in range(100):
    currentMouseX, currentMouseY = pyautogui.position()
    print(f'mouse is at{currentMouseX},{currentMouseY}')
    time.sleep(1)
"""
