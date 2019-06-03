#! python
# emailDeleter.py - Deletes all emails from inbox
# that match the given subject line criteria

import imapclient, pyzmail, os, imaplib

# Increase imap size limit to 10M bytes
imaplib._MAXLINE = 10000000


# Set email and prompt for email password
email='PBShin96@gmail.com'
#print('Please enter password(app-specific password for gmail):')
password=input('Please enter password(app-specific password for gmail): ')


# Scan through emails to find emails from Google's Mail Delivery Subsystem
imapObj=imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj=imaplib.IMAP4_SSL('imap.gmail.com', 993)
imapObj.login(email, password)
#pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=False)
UIDs=imapObj.search(['FROM', 'mailer-daemon@googlemail.com'])
print(UIDs)

imapObj.delete_messages(UIDs)

rawMessages=imapObj.fetch(UIDs, ['BODY[]'])
#pprint.pprint(rawMessages)
#for i in range(len(UIDs)):
#    message=pyzmail.PyzMessage.factory(rawMessages[UIDs[i]][b'BODY[]'])
#print(message.text_part.get_payload().decode(message.text_part.charset))
#bodyText=message.text_part.get_payload().decode(message.text_part.charset)
