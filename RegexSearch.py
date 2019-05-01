#! python
# RegexSearch.py
# Searches through all .txt files in current folder and print any found
# matches to user inputted expressions

import re, os

# Create variable for current directory
cwd = os.path.abspath('.')

# Create list containing all folders in current directory
cwdlist = os.listdir(cwd)

# Create regex object for .txt files
txtRegex = re.compile(r'(\w+)(.txt)')

# Create list containing all .txt files filtered out of current directory
txtlist = []
for file in cwdlist:
    mo = txtRegex.search(file)
    if mo != None:
        #print(mo.group())
        txtlist.append(file)
        
#print(cwdlist)
#print(txtlist)       

# Prompt user to input expression and convert into regex object
print('Please enter the expression to be searched for:')
inputEx = input()
inputRegex = re.compile(inputEx) #figure out how to convert inputEx to raw str var

# Loop through list of txt files to search for user inputted expression
matchlist = []
for file in txtlist:
    # open each file
    txtFile = open(file)
    # create object to hold text from file
    content = txtFile.read()
    #print(content)
    # Create match object for test
    mo = inputRegex.search(content)
    # Add file with match to a list
    if mo != None:
        matchlist.append(file)

print(matchlist)


