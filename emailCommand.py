#! python
# emailCommand.py - check email every 15 min for email containing instructions and runs

import time, datetime, imapclient, pyzmail, os, subprocess, imaplib, pprint, sys

# Increase imap size limit to 10M bytes
imaplib._MAXLINE = 10000000

# Set program to run every 15 minutes

# Set email and prompt for email password
email='PBShin96@gmail.com'
print('Please enter password(app-specific password for gmail):')
password=input()
while True:
    try:
        # Scan through emails to find emails with "Instructions" in subject line
        imapObj=imapclient.IMAPClient('imap.gmail.com', ssl=True)
        imapObj.login(email, password)
        #pprint.pprint(imapObj.list_folders())
        imapObj.select_folder('INBOX', readonly=True)
        UIDs=imapObj.search(['SUBJECT', 'Python Email Instructions', 'SINCE', '01-May-2019'])
        #print(UIDs)
        rawMessages=imapObj.fetch(UIDs, ['BODY[]'])
        #pprint.pprint(rawMessages)
        message=pyzmail.PyzMessage.factory(rawMessages[UIDs[0]][b'BODY[]'])
        #print(message.get_subject())
        #print(message.text_part.get_payload().decode(message.text_part.charset))
        exec(message.text_part.get_payload().decode(message.text_part.charset))
        for i in range(int(datetime.timedelta(minutes=15).total_seconds())):
            time.sleep(1)
    except KeyboardInterrupt:
        print('Program Ended')
        sys.exit()
        
# Example instructions to be sent via email:
#def Instructions():
#    process=subprocess.Popen([os.path.join('c:', os.sep, 'Applications',\
#                                           'TextEdit.app'), \
#                              os.path.join('c:', os.sep, 'Users', 'Phil', \
#                                           'Documents', 'python', \
#                                           'emailCommand.txt')])
#print('Poll:')
#print(process.poll())
#print('Wait:')
#print(process.wait())
