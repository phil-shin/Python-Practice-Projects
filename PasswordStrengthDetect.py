#! python
# PasswordStrengthDetect.py
# This program determines if an inputted password string is 'strong' via regex objects

import re

def passwordStrDetect(password):
    lenRegex = re.compile(r'(\w{8,})') #regex object for min length of 8 characters
    upperRegex = re.compile(r'[A-Z]')  #regex object for a uppercase character
    lowerRegex= re.compile(r'[a-z]')   #regex object for lowercase character
    numRegex = re.compile(r'(\d)+')     #regex object for digit character
    moLen=lenRegex.search(password)
    moUpper=upperRegex.search(password)
    moLower=lowerRegex.search(password)
    moNum=numRegex.search(password)
    #print(moLen)   #debug
    #print(moUpper) #debug
    #print(moLower) #debug
    #print(moNum)   #debug
    if moLen==None or moUpper==None or moLower==None or moNum== None:
                print('Password is invalid')
    else:
        print('Password is valid.')
         

print('Please enter valid password:')
password = input()
passwordStrDetect(password)
