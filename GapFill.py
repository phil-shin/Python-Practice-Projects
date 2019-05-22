#! python
# GapFill.py
# Program to
# Locate any gaps in list of numbered files and
# change file names to close gaps

import os, shutil

#Set working directory
wd = os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python', 'GapFill') 
#print(wd)

# Set file base name
basename = 'spam'

#Create sorted list of numbered files
wdlist = os.listdir(wd)
#print(wdlist)
sortedlist = sorted(wdlist)
#print(sortedlist)
# Indices for file number formatting
i=1
j=1
# Loop through sorted list of files
for file in sortedlist:
    if file.startswith('.'):
        continue
    numFormat = '{:03}'.format(i)
    #print(file)
    fullname = basename + numFormat + '.txt'
    #print(fullname)
    # Check if file name matches correct file name in list
    if file != fullname:
        # Rename all files properly if gap is found
        for file in sortedlist:
            if file.startswith('.'):
                continue
            #print(file)
            numFormat2 = '{:03}'.format(j)
            #print(numFormat2)
            newFile = basename + numFormat2 + '.txt'
            filepath = os.path.join(wd, file)
            #print(filepath)
            newFilepath = os.path.join(wd, newFile)
            #print(newFilepath)
            shutil.move(filepath, newFilepath)
            j+=1
        break
    i+=1            


