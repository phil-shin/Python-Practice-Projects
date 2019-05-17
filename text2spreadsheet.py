#! python
# text2spreadsheet.py
# Copies lines within text files in directory to columns of spreadsheet

import openpyxl, os

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python')
print(cwd)

# Open text files and create list object for text string lines
col1File=open(os.path.join(cwd, 'col1.txt'))
col1Content=col1File.readlines()
col2File=open(os.path.join(cwd, 'col2.txt'))
col2Content=col2File.readlines()
col3File=open(os.path.join(cwd, 'col3.txt'))
col3Content=col3File.readlines()
contentList=[col1Content, col2Content, col3Content]

# Write lists into columns of spreadsheet
wb=openpyxl.Workbook()
sheet=wb.active

for col in range(1, len(contentList)+1):
    print(col)
    for row in range(1, len(contentList[col-1])+1):
        print(row)
        sheet.cell(row=row, column=col).value=contentList[col-1][row-1]
        
# Save spreadsheet
wb.save('text2spreadsheet.xlsx')

