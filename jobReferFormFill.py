#! python
# jobReferFormFill.py - Fills out job referral form at open window
# and hits submit

import pyautogui, time

# Set First name form and Send button coordinates
firstNameForm= (864, 480)
sendButton= (1166, 702)

# Set Form Info.
formData = {'First Name': '', 'Last Name':'', \
            'Email':'', 'Phone':'',\
            'Country':'united state'}

# Fill out form
print("Entering %s's info..." % formData['First Name'])
pyautogui.click(firstNameForm[0], firstNameForm[1])
pyautogui.typewrite(formData['First Name']+'\t')
pyautogui.typewrite(formData['Last Name']+'\t')
pyautogui.typewrite(formData['Email']+'\t')
pyautogui.typewrite(formData['Phone']+'\t')
pyautogui.typewrite(formData['Country'])

# Click Send button
pyautogui.click(sendButton[0], sendButton[1])

print('Done')
