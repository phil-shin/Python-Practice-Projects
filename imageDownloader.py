#! python
# imageDownloader.py - searches unsplash.com for category of photos(i.e. "study")
# and downloads a set number(50) of the resulting images

import os, requests, bs4

# Get base url, set variable for search category, get url for search category
baseUrl='http://unsplash.com'
searchCat='study'
searchUrl=baseUrl+'/search/photos/'+searchCat
os.makedirs('study_photos', exist_ok=True)

# Download search results page, create bs4 object
print('Downloading page %s...' % searchUrl)
res=requests.get(searchUrl)
res.raise_for_status()

soup=bs4.BeautifulSoup(res.text)

# Obtain list of image elements
imageElem=soup.select('._3oSvn img') 
#imageElem=soup.select('div[class="_3oSvn IEpfq"]img')
if imageElem == []:
    print('Could not find images')
else:
    # Loop through list of image elements for first [50] images
    for image in imageElem:
        try:
            # Get source url of image
            imageUrl=imageElem[imageElem.index(image)].get('src')
            # Download source url
            print('Downloading image %s...' % imageUrl)
            res=requests.get(imageUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip image if error downloading image source url
            continue
        # Save image into new folder
        imageFile=open(os.path.join('study_photos', 'image'+str(imageElem.index(image))+'.png'), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
print('Done')
