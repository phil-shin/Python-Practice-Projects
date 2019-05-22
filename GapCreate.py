#! python
# GapCreate.py
# Insert gap in a list of numbered files for a new file to be added

import os, shutil

# Set working directory
wd = os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python', 'GapFill') 
print(wd)

# Set file base name
basename = 'spam'

#Create sorted list of numbered files
wdlist = os.listdir(wd)
sortedlist=sorted(wdlist)

# Prompt user for gap location
print('Please enter the file iteration to be inserted:')
newFile = int(input())

# Loop through sorted list of files
for i in reversed(range(newFile,(len(sortedlist)))):
    print(i)
    newFormat = '{:03}'.format(i+1)
    print(newFormat)
    newName = basename + newFormat + '.txt'
    print(newName)
    oldPath = os.path.join(wd, sortedlist[i])
    print(oldPath)
    newPath = os.path.join(wd, newName)
    print(newPath)
    shutil.move(oldPath, newPath)
   
