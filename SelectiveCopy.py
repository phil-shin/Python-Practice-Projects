#! python
# SelectiveCopy.py
# Filters to find .txt files in a folder tree and copy them into a new folder

import os, re, shutil

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python')
#print(cwd)

#Create regex object for .txt files
txtRegex = re.compile(r'(\w+)(.txt)')

# Create path for back up folder
backupPath = os.path.join(cwd, 'backup')

# Loop to walk through folder tree
for folderName, subfolders, filenames in os.walk(cwd):
    #print(folderName)
    #print(subfolders)
    #print(filenames)
    for filename in filenames:
        if folderName == backupPath:
            continue # Ignore files already in backup folder
        else:
            #print(filename)
            mo = txtRegex.search(filename)
            if mo != None:
                currentPath = os.path.join(cwd, folderName, filename)
                shutil.move(currentPath, backupPath) #Move file to backup folder
