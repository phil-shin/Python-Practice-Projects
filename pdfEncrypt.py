#! python
# pdfEncrypt.py - encrypts all PDF files in a folder and its subfolders

import os, PyPDF2, shutil

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'PS81581', 'AppData', 'Local', 'Programs', 'Python', 'Python37')
os.chdir(cwd)

# Walk through directory
for folder, subFolders, fileNames in os.walk(cwd):
    for file in fileNames:
        if file.endswith('.pdf'):
            #print(folder)
            #print(file)
            # Check to make sure pdf file is not already encrypted
            try:
                # Loop through pages of PDF file & copy onto new PDF file
                pdfFile=open(file, 'rb')
                pdfReader=PyPDF2.PdfFileReader(pdfFile)
                pdfWriter=PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                # Add password encryption to new PDF file
                pdfWriter.encrypt('password')
                encryptPdf=open('encrypted'+file, 'wb')
                pdfWriter.write(encryptPdf)
                encryptPdf.close()
                # Overwrite old pdf file with new encrypted PDF file copy
                shutil.move(os.path.join('.','encrypted'+file), os.path.join('.',file))
            except PyPDF2.utils.PdfReadError:
                continue
