#! python
# ymcaSched.py - Downloads and opens the image of the current gym
# schedule for the Beaver Dam, WI YMCA

import os, requests, bs4, subprocess

# Set url for ymca gym schedule
url = 'https://www.theydc.org/schedules'

# Download page and create bs4 object
print('Downloading page %s...' % url)
res=requests.get(url)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

# Locate gym schedule image link element
schedElem=soup.select('#wid51551 a')

# Get source url of image
imageurl=schedElem[0].get('href')
print('Downloading image %s...' % imageurl)
res=requests.get(imageurl)
res.raise_for_status()

# Download image onto desktop
imagePath=os.path.join('c:', os.sep, 'Users', 'PS81581', 'Desktop', \
                            'ymca_gym_sched.png')
imageFile=open(imagePath)
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()
               
# Open image
process=subprocess.Popen(['start', imagePath], shell=True)
               
