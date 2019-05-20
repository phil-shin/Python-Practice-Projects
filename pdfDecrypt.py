#! python
# pdfDecrypt.py - decrypts all encrypted PDF files in a folder and its subfolders

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
            # or if decryption password is incorrect
            try:
                pdfFile=open(file, 'rb')
                pdfReader=PyPDF2.PdfFileReader(pdfFile)
                pdfReader.decrypt('password')
                # Copy pages of encrypted pdf file to new decrypted pdf file
                pdfWriter=PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                decryptPdf=open('decrypted'+file, 'wb')
                pdfWriter.write(decryptPdf)
                decryptPdf.close()
                # Overwrite old encrypted pdf file with new decrypted pdf file copy
                shutil.move(os.path.join('.','decrypted'+file), os.path.join('.',file))
            except KeyError:
                continue #Passes over decrypted pdf files
            except PyPDF2.utils.PdfReadError:
                print('Incorrect password') #Error message for incorecct pdf file password 
                continue 
