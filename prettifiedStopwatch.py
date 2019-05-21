#! python
# prettifiedStopwatch.py - simple stopwatch program that neatly outputs
# total time duration and laptimes & copies output data to clipboard

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
outputString=''

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        # String variables:
        lapNumString=str(lapNum)
        totalString=str(totalTime)
        lapTimeString=str(lapTime)
        # Print Strings
        output='Lap #'.ljust(5)+lapNumString.rjust(3)+':'+totalString.rjust(5)+'('+lapTimeString.rjust(5)+')'#,sep='', end=''
        print(output,end='')
        outputString= outputString+output+'\n'
        #outputString+='\n'
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    #print(outputString)
    pyperclip.copy(outputString)
    print('\nDone.')
