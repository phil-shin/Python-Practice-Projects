# python!
# regexStrip.py
# Recreates strip() function using regex objects
# Second argument will replace preceeding and following whitespaces with character

import re

def regexStrip(arg, args = None):
    regexStrip=re.compile(r'''
        (\s*)                    #0 or more space characters
        (\w+)                    #first character of internal string
        ([\w\s]*)                  #1 or more word characters
        (\w+)                    #last character of internal string
        (\s*)                  #0 or more space characters
        ''', re.VERBOSE)
    mo=regexStrip.search(arg)
    #print(stringg)
    #print('-'+mo.group(0)+'-')
    #print('-'+mo.group(1)+'-')
    #print('-'+mo.group(2)+'-')
    #print('-'+mo.group(3)+'-')
    #print('-'+mo.group(4)+'-')
    #print('-'+mo.group(5)+'-')
    if args == None:
        print(mo.group(2)+mo.group(3)+mo.group(4))
        #print('no arg')
    else:
        spaceCount1 = len(str(mo.group(1)))
        spaceCount2 = len(str(mo.group(5)))
        new1 = args * spaceCount1
        #print(type(new1))
        new2 = args * spaceCount2
        print(regexStrip.sub(new1+'\\2\\3\\4', arg),end='')
        print(new2)
        #print('arg')
        

#print('Please input a string to strip:')
arg='   a bc   '
args='8'
regexStrip(arg, args)
    
