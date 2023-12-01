import pyautogui
import time

text_to_spam = input("Please enter text to spam. ")

time.sleep(5)
for i in range(10):
    # pyautogui.write("@VK3546")
    pyautogui.write(text_to_spam)
    pyautogui.press('enter')
