import pyautogui # For typing!
import time # So it doesn't write the entire thing at once!
import keyboard # So you can stop the program!

time.sleep(3)

def shrek():
    while True: #STANDARD COMBO PROCEDURE 
        if keyboard.is_pressed('SHIFT'):
            if keyboard.is_pressed('Z'):
                print("Script Cancelled!")
                break #STOP SCRIPT WHEN KEYBIND TOGGLED
        if = open("shrekmovie.txt", 'r') # Open the file
        for word in f:
            time.sleep(0.50)
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            
