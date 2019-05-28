#! python
# linkVerify.py - attempts to download every linked page on a given page
# and prints out broken links

import requests, bs4

# Set baseurl & url
url='https://automatetheboringstuff.com/chapter11/'
baseUrl='https://automatetheboringstuff.com'

# Download page, create bs4 object
print('Downloading page %s...' % url)
res=requests.get(url)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

# Obtain list of elements containing links
linkElem=soup.find_all('a', href=True)
if linkElem == []:
    print('No links found')
for link in linkElem:
    linkUrl=linkElem[linkElem.index(link)].get('href')
    #print(linkUrl)
    #if linkUrl == None:
    #    continue
    if linkUrl.startswith('//'):
        linkUrl='https:'+linkUrl
    if not linkUrl.startswith('http'):
        linkUrl=baseUrl+linkUrl
    #print('Downloading page %s...' % linkUrl)
    try:
        res=requests.get(linkUrl)
        res.raise_for_status()
    except requests.exceptions.SSLError:
        print('Link SSL certificate failure:'+linkUrl+'; link skipped')
        continue
    except requests.exceptions.HTTPError:
        print('404 Error Found:'+linkUrl)
    #print('Link verified')
print('Done')
