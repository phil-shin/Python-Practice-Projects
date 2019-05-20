#! python
# customInvite.py - Create custom, styled invites
# on a word doc from a list of guest names

import os, docx

# Set working directory
cwd = os.path.join('c:', os.sep, 'Users', 'PS81581', 'AppData', 'Local', 'Programs', 'Python', 'Python37')
os.chdir(cwd)

# Load guest list from .txt file
guestListFile=open('guestlist.txt')
guestList=guestListFile.read().splitlines()
print(guestList)

# Create single page custom invite for each guest in a word doc
doc = docx.Document()
i=0
for guest in guestList:
    paraObj1=doc.add_paragraph('It would be a pleasure to have the company of')
    paraObj1.style='Quote'
    doc.paragraphs[i].runs[0].add_break()
    i+=1
    paraObj2=doc.add_paragraph(guest)
    paraObj2.style='Caption'
    doc.paragraphs[i].runs[0].add_break()
    i+=1
    paraObj3=doc.add_paragraph('at 11010 Memory Lane on the Evening of')
    paraObj3.style='Quote'
    doc.paragraphs[i].runs[0].add_break()
    i+=1
    paraObj4=doc.add_paragraph('April 1st')
    paraObj4.style='Subtitle'
    doc.paragraphs[i].runs[0].add_break()
    i+=1
    paraObj5=doc.add_paragraph('at 7 o\'clock')
    paraObj5.style='Quote'
    doc.paragraphs[i].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
    i+=1
doc.save('customInvite.docx')
