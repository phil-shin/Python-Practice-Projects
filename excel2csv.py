#! python
# excel2csv.py - converts every spreadsheet in a directory to individual csv files

import os, openpyxl, csv

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'PS81581', 'AppData', 'Local', 'Programs', 'Python', 'Python37', 'excel2csv')
os.chdir(cwd)
print(cwd)

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]
        # Create the CSV filename from the Excel filename and sheet title.
        csvFileName=excelFile+'_'+sheetName+'.csv'
        # Create the csv.writer object for this CSV file.
        csvFileObj=open(os.path.join(cwd, csvFileName), 'w', newline='')
        csvWriter=csv.writer(csvFileObj)
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row+1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column+1):
                # Append each cell's data to rowData.
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
            # Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)
        csvFileObj.close()
