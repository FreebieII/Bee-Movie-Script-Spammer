import pyautogui, time # Import packages

time.sleep(5) # starts running in 5 seconds
s = open("beemovie", "r") #Opens beemovie file 
for word in s:
    pyautogui.typewrite(word) #writes the word per line
    pyautogui.press("enter") #presses enter
