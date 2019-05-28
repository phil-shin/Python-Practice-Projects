#! python
# comicDownloader.py - check multiple websites to see if the latest
# comic has been downloaded. If not, the latest comic will be downloaded onto
# the desktop

import os, requests, bs4

# Create list of urls for comic websites
urls = [
    'https://xkcd.com',
    'http://www.lefthandedtoons.com/',
    'https://www.buttersafe.com/',
    'https://www.savagechickens.com/'
]
os.makedirs('comics', exist_ok=True)
desktopPath=os.path.join('c:', os.sep, 'Users', 'PS81581', 'Desktop')

# Loop through websites, download page, create bs4 object
for url in urls:
    print('Downloading page %s' % url)
    try:
        res=requests.get(url)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
    except requests.exceptions.SSLError:
        print('Link SSL certificate failure')
        continue
    # Obtain list of image elements
    if url == 'https://xkcd.com':
        imageElem=soup.select('#comic img')
    elif url == 'http://www.lefthandedtoons.com/':
        imageElem=soup.select('#comicwrap img')
    elif url == 'https://www.buttersafe.com/':
        imageElem=soup.select('#comic img')
    elif url == 'https://www.savagechickens.com/':
        imageElem=soup.select('#maincontent img')
    if imageElem == []:
        print('Could not find comic')
        continue
    # Get latest comic image source url
    imageUrl='http:'+imageElem[0].get('src')
    # Check if image is already downloaded on desktop
    fileName=os.path.join(desktopPath, os.path.basename(imageUrl))
    if os.path.exists(fileName):
        print('Latest comic from %s already downloaded' % url)
        continue
    # Download source url
    res=requests.get(imageUrl)
    res.raise_for_status()
    # Save image to desktop
    imageFile=open(fileName, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
print('Done')
