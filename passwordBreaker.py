#! python
# passwordBreaker.py - decrypts a pdf file by trying every possible english word
# Program does not work for PDFs secured wtih enhanced security

import os, PyPDF2

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'PS81581', 'AppData', 'Local', 'Programs', 'Python', 'Python37')
os.chdir(cwd)

# Store dictionary list into list object
dictionaryFile=open('dictionary.txt')
dictionary=dictionaryFile.read().splitlines()

# Create pdfReader object of pdf file
pdfFile=open('passwordBreaker.pdf', 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)

# Loop through list, trying upper and lower case forms, to decrypt pdf
for word in dictionary:
    if pdfReader.decrypt(word.lower()) ==1 or pdfReader.decrypt(word.upper()) ==1:
        print('PDF Decrypted, password is:')
        print(word)
        break
