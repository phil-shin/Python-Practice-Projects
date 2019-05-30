#! python
# autoUnsub.py - searches through emails, finds unsubscribe links, and
# automically opens them in a browser

import smtplib, imapclient, pprint, webbrowser, imaplib, bs4

# Increase imap size limit to 10M bytes
imaplib._MAXLINE = 10000000

# Set email and prompt for email password
email='PBShin96@gmail.com'
print('Please enter password(app-specific password for gmail):')
password=input()

# Scan through emails to find emails with unsubscribe links
imapObj=imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(email, password)
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
UIDs=imapObj.search(['OR SUBJECT unsubscribe SUBJECT Unsubscribe'])
rawMessages=imapObj.fetch(UIDs, ['BODY[]'])
for messageID in rawMessages:
    message=pyzmail.PyzMessage.factory(rawMessages[messageID]['BODY[]'])
    soup=bs4.BeautifulSoup(message)
    unsubElem=soup.select('
    # Open unsubscribe links 
