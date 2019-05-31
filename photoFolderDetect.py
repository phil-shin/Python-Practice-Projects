#! python
# photoFolderDetect.py - walks through directories in computer and detects
# folders with photo files presenting over half the files

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith('.png' or '.jpg'):
            numNonPhotoFiles += 1
            continue    # skip to next filename
        # Completely skip files in recycling bin
        elif filename.startswith('$'):
            continue
        try:
            # Open image file using Pillow.
            image=Image.open(os.path.join('c:', os.sep, foldername, filename))
        # Skip past files that cannot be openned / are not supported
        except OSError:
            print('Could not open file: '+os.path.join('c:', os.sep, foldername, filename))
            continue
        # Check if width & height are larger than 500.
        width, height = image.size
        if (width and height) > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
    # If more than half of files were photos,
    # print the absolute path of the folder.
    numTotalFiles=len(filenames)
    if numPhotoFiles > (numTotalFiles / 2):
        print(os.path.join('c:', os.sep, foldername))
