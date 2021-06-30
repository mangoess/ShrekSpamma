import pyautogui # For typing!
import time # So it doesn't write the entire thing at once!
import keyboard # So you can stop the program!

def shrek():
    f = open("moviefile.txt", 'r') # Open the file, r is for raw referring to the method to get the file location
    for word in f:
        time.sleep(0.50)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        if keyboard.is_pressed('SHIFT'):
            if keyboard.is_pressed('Z'):
                print("Script Cancelled!")
                break #STOP SCRIPT WHEN KEYBIND TOGGLED
            else:
                pass
print("5 Second timer started, hold Shift and Z to stop")
time.sleep(3)
print("3 Seconds passed, starting soon")
time.sleep(2)
print("Shrek has been awoken!\n")
shrek()
