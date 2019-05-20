#! python
# Sizefilter.py
# Filter through folder tree and lists out large files

import os, shutil

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python')

# Loop to walk through folder tree
for folderName, subfolders, filenames in os.walk(cwd):
    #print(folderName)
    #print(subfolders)
    #print(filenames)
    for filename in filenames:
        absPath = os.path.join(cwd, folderName, filename)
        if os.path.getsize(absPath) >= 100000: #Set size filter 
            print(absPath)
