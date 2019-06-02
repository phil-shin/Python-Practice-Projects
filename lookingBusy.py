#! python
# lookingBusy.py - slightly nudges mouse cursor once every 10 minutes

import time, datetime, pyautogui, sys

print('Press cntrl + C to end program.')

# Set program to run every 10 minutes
while True:
    try:
        pyautogui.moveRel(1,0)
        time.sleep(datetime.timedelta(minutes=10).total_seconds())
        pyautogui.moveRel(-1,0)
        time.sleep(datetime.timedelta(minutes=1).total_seconds())
        # Allow for cntl+C to interrupt program
    except KeyboardInterrupt:
        print('Program Ended')
        sys.exit()
    
