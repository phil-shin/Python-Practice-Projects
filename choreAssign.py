#! python
# choreAssign.py - Assign random chore from list to each person in list
# and emails them a reminder
# Additional feature: ensures unique chore assignment to person (no repeated chores)
# Additional feature: re-sends unique chore assignment automatically once per week

import time, datetime, smtplib, sys, random

  
# Create dictionary of names and email addresses
#people = ['Alice', 'Bob', 'Carol', 'David']
emails={'Alice':{'email':'alice@gmail.com', 'choreRec':[]},\
        'Bob':{'email':'bob@gmail.com', 'choreRec':[]},\
        'Carol':{'email':'carol@gmail.com', 'choreRec':[]},\
        'David':{'email':'david@gmail.com', 'choreRec':[]}}

# Prompt for email password
print('Please enter email password:')
password=input()

try:
    for i in range(4):
        #print(i)
        chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
        for name in emails:
            # Email random chore selection to each recipient
            randomChore=random.choice(chores)
            while randomChore in emails[name]['choreRec']:
                randomChore=random.choice(chores)
            #print('non-repeated '+randomChore)
            chores.remove(randomChore)
            smtpObj=smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login('PBShin96@gmail.com', password)
            body='Subject: Chore Assignment\nDear %s,\nYour chore assignment is %s' % (emails[name], randomChore)
            emailStatus=smtpObj.sendmail('PBShin96@gmail.com', emails[name]['email'], body)
            if emailStatus !={}:
                print('Issue sending email to %s' % (emails[name]['email']))
                sys.exit()
            else:
                print('Sending email to %s...' % (emails[name]['email']))
            # Update chore record and avoid repetition
            emails[name]['choreRec'].append(randomChore)
            smtpObj.quit()
        # Schedule program to run once a week
        #time.sleep(datetime.timedelta(days=7).total_seconds())
        for i in range(604800): # Allows for KeyboardInterrupt within 1 second
            time.sleep(1)
except KeyboardInterrupt:
    print('Program Ended Early')
    sys.exit()
#print(emails['Alice']['choreRec'],\
#      emails['Bob']['choreRec'],\
#      emails['Carol']['choreRec'],\
#      emails['David']['choreRec'])
print('Program Ended')
