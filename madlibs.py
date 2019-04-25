# python!
# madlibs.py
# Creates a Mad Libs program that edits a text file based on user inputs

print('Please enter an Adjective:')
adj1=input()
print('Please enter an Adjective:')
adj2=input()
print('Please enter an Noun:')
noun1=input()
print('Please enter a Verb:')
verb1=input()
print('Please enter a Noun:')
noun2=input()

madlibsFile = open('madlibs.txt', 'w')
madlibsFile.write('The ' + adj1 + ' dog went down to the ' + adj2 + ' restaurant \
and ran into a ' + noun1 + '. He quickly ' + verb1 + ' to the ' + noun2 + '.')
madlibsFile.close()
madlibsFile = open('madlibs.txt')
content = madlibsFile.read()
madlibsFile.close()
print(content)


