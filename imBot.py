#! python
# imBot.py - program that send message to myself when at facebook messenger page
# Positioning is based on facebook messager page open on a Google Chrome
# browser window open at full screen on a MacBook Pro

import pyautogui, time

# Set compose message button coordinates and click
composeButton = (336, 139)
pyautogui.doubleClick(composeButton[0], composeButton[1])

# Select "To:" form
pyautogui.click(350, 139)

# Type 'phil shin' and select to send message
pyautogui.typewrite('phil shin')
time.sleep(1)
pyautogui.typewrite(['enter'])

# Send message
pyautogui.typewrite(['h', 'i', 'enter'])
