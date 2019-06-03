#! python
# emailInstructions.py - example instructions to be sent via email and executed
# within 'emailCommand.py' program

import subprocess, os

#process=subprocess.Popen([os.path.join('c:', os.sep, 'Applications',\
#                                       'Microsoft Word.app'), \
#                                       os.path.join('c:', os.sep, 'Users', \
#                                                    'Phil', \
#                                       'Documents', 'python', \
#                                       'emailCommand.docx')], shell=True)
#print('After Popen:')
#print('Poll:')
#print(process.poll())
#print('Wait:')
#print(process.wait())

process=subprocess.Popen(['start', os.path.join('c:', os.sep, 'Users', 'Phil', \
                                                'Documents', 'python', \
                                                'emailCommand.txt')],\
                         shell=True)
print(process.poll())
print(process.wait())
#os.system(os.path.join('c:', os.sep, 'Users', 'Phil', 'Documents', 'python', \
#                       'emailCommand.txt'))
