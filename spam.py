import pyautogui
import time
import keyboard

time.sleep(3)

f = open("shrekmovie.txt", 'r') #PHYSICAL SPAM SCRIPT
for word in f:
    time.sleep(0.50)
    pyautogui.typewrite(word)
    pyautogui.press("enter")

while True: #STANDARD COMBO PROCEDURE 
    if keyboard.is_pressed('CTRL'):
        if keyboard.is_pressed('X'):
            break #STOP SCRIPT WHEN KEYBIND TOGGLED
            
