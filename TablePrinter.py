#TablePrinter.py
# program that reformats list of lists into right justified columns
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i]=len(tableData[i][j])
    #print(colWidths)
    #print(len(tableData[0]))
    #print(len(tableData))
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

            
                
