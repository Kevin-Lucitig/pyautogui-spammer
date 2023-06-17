import pyautogui
import time

def spamming(text):
    pyautogui.typewrite(text)

while True:
    text_to_type = 'your text' #replace your text with the actuall text you want to spam. but dont delete the strings!!!
    pyautogui.press('enter')
    spamming(text_to_type)
    time.sleep(0.1)
