import pyautogui, time
time.sleep(3)
f = open("shrekmovie.txt", 'r')
for word in f:
    time.sleep(0.50)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
